# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Cloud logging client library for Cloud ML batch prediction dataflow job.
"""
import logging
import six

# Payload types supported.
_PAYLOAD_TYPES = set({"textPayload", "jsonPayload"})
# The resource type. It applies to both training jobs and batch prediction jobs.
_RESOURCE_TYPE = "ml_job"
# The job id label.
_JOB_ID_LABEL = "job_id"

# Field names for error-related fields in the logEntry. See
# proto: google.cloud.ml.api.v1beta1.PredictionLogEntry
_MESSAGE_KEY = "message"
_ERROR_MESSAGE_KEY = "error_detail"
_ERROR_DETAIL_KEY = "detail"
_ERROR_INPUT_SNIPPET_KEY = "input_snippet"

# This is to make logging format compatible to the log entries generated by
# converting protobuf to JSON during training.
FIXED_ENTRY = {
    "@type":
    "type.googleapis.com/google.cloud.ml.api.v1beta1.PredictionLogEntry"
}


class LogSeverity(object):
  """Log severity enums.

  Ref: https://cloud.google.com/logging/docs/api/reference/
  rest/v2/LogEntry#LogSeverity
  """
  DEFAULT = 0
  DEBUG = 100
  INFO = 200
  NOTICE = 300
  WARNING = 400
  ERROR = 500
  CRITICAL = 600
  ALERT = 700
  EMERGENCY = 800


class MLCloudLoggingClient(object):
  """Cloud logging client.

  A wrapper around google.cloud.logging object. It provides more friendly
  interface as callers don't need to provide some fixed fields, such as
  project id, job id, resource type, logger name, the resource type.
  """

  def __init__(self, logger, logger_name, job_id, payload_type):
    self._job_id = job_id
    self._payload_type = payload_type
    self._logger = logger
    self._logger_name = logger_name

  def write_error_message(self, error_message, input_snippet):
    """Create an error mess and input snippet to cloud logging."""
    error_message = unicode(error_message, errors="replace")
    log_entry = {
        _MESSAGE_KEY: error_message,
        _ERROR_MESSAGE_KEY: {
            _ERROR_DETAIL_KEY: error_message,
            _ERROR_INPUT_SNIPPET_KEY: input_snippet
        }
    }
    log_entry.update(FIXED_ENTRY)

    self.write_entries(log_entry, severity=LogSeverity.ERROR)

  def write_entries(self, message, severity=LogSeverity.DEFAULT):
    """Write log entries to cloud logging.

    Args:
      message: A text string or a dict. The log to write. Its type depends on
               the payload type.
      severity: the LogSeverity enum. Severity of the log entry.
    """
    self._logger.write_entries(
        entries=[{self._payload_type: message, "severity": severity}],
        logger_name=self._logger_name,
        resource={"type": _RESOURCE_TYPE,
                  "labels": {_JOB_ID_LABEL: self._job_id,}})

  @classmethod
  def create(cls, project, job_id, log_name, payload_type,
             external_logger=None):
    """Create ML cloud logging client.

    Args:
      project: String The project the logs will be sent to.
      job_id: String Used to populate the job_id in the resource type.
      log_name: String the name for the logs.
      payload_type: String. It is either jsonPayload or textPayload.
      external_logger: a logger obj. Currently it is for dependency injection
                       in testing.

    Raises:
      ValueError: if any input is not legitimate.

    Returns:
      MLCloudLoggingClient obj.
    """
    if not project or not isinstance(project, six.string_types):
      raise ValueError("Project must be a non-empty string.")

    if not job_id or not isinstance(job_id, six.string_types):
      raise ValueError("Job_id must be a non-empty string.")

    if payload_type not in _PAYLOAD_TYPES:
      raise ValueError("Unknown payload type: %s" % payload_type)

    if not external_logger:
      try:
        # We import the module locally because it is not available in google3
        # where unittest would must depend on.
        import google.cloud.logging   # pylint: disable=g-import-not-at-top
        client = google.cloud.logging.Client(project=project, use_gax=False)
        logger = client.logging_api
      except Exception as e:
        logging.info("Failed to initialize cloud logging client.")
        raise e
    else:
      # This is mainly for testing purpose.
      logger = external_logger

    logger_name = "projects/%s/logs/%s" % (project, log_name)
    return MLCloudLoggingClient(logger, logger_name, job_id, payload_type)
