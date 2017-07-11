"""Generated message classes for appengine version v1alpha.

The App Engine Admin API enables developers to provision and manage their App
Engine applications.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'appengine'


class AppengineAppsAuthorizedCertificatesCreateRequest(_messages.Message):
  """A AppengineAppsAuthorizedCertificatesCreateRequest object.

  Fields:
    authorizedCertificate: A AuthorizedCertificate resource to be passed as
      the request body.
    parent: Name of the parent Application resource. Example: apps/myapp.
  """

  authorizedCertificate = _messages.MessageField('AuthorizedCertificate', 1)
  parent = _messages.StringField(2, required=True)


class AppengineAppsAuthorizedCertificatesDeleteRequest(_messages.Message):
  """A AppengineAppsAuthorizedCertificatesDeleteRequest object.

  Fields:
    name: Name of the resource to delete. Example:
      apps/myapp/authorizedCertificates/12345.
  """

  name = _messages.StringField(1, required=True)


class AppengineAppsAuthorizedCertificatesGetRequest(_messages.Message):
  """A AppengineAppsAuthorizedCertificatesGetRequest object.

  Enums:
    ViewValueValuesEnum: Controls the set of fields returned in the GET
      response.

  Fields:
    name: Name of the resource requested. Example:
      apps/myapp/authorizedCertificates/12345.
    view: Controls the set of fields returned in the GET response.
  """

  class ViewValueValuesEnum(_messages.Enum):
    """Controls the set of fields returned in the GET response.

    Values:
      BASIC_CERTIFICATE: <no description>
      FULL_CERTIFICATE: <no description>
    """
    BASIC_CERTIFICATE = 0
    FULL_CERTIFICATE = 1

  name = _messages.StringField(1, required=True)
  view = _messages.EnumField('ViewValueValuesEnum', 2)


class AppengineAppsAuthorizedCertificatesListRequest(_messages.Message):
  """A AppengineAppsAuthorizedCertificatesListRequest object.

  Fields:
    pageSize: Maximum results to return per page.
    pageToken: Continuation token for fetching the next page of results.
    parent: Name of the parent Application resource. Example: apps/myapp.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class AppengineAppsAuthorizedCertificatesPatchRequest(_messages.Message):
  """A AppengineAppsAuthorizedCertificatesPatchRequest object.

  Fields:
    authorizedCertificate: A AuthorizedCertificate resource to be passed as
      the request body.
    name: Name of the resource to update. Example:
      apps/myapp/authorizedCertificates/12345.
    updateMask: Standard field mask for the set of fields to be updated.
      Updates are only supported on the certificate_raw_data and display_name
      fields.
  """

  authorizedCertificate = _messages.MessageField('AuthorizedCertificate', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class AppengineAppsAuthorizedDomainsListRequest(_messages.Message):
  """A AppengineAppsAuthorizedDomainsListRequest object.

  Fields:
    pageSize: Maximum results to return per page.
    pageToken: Continuation token for fetching the next page of results.
    parent: Name of the parent Application resource. Example: apps/myapp.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class AppengineAppsDomainMappingsCreateRequest(_messages.Message):
  """A AppengineAppsDomainMappingsCreateRequest object.

  Fields:
    domainMapping: A DomainMapping resource to be passed as the request body.
    noManagedCertificate: Whether a managed certificate should be provided by
      App Engine. If true, a certificate ID must be manaually set in the
      DomainMapping resource to configure SSL for this domain. If false, a
      managed certificate will be provisioned and a certificate ID will be
      automatically populated.
    parent: Name of the parent Application resource. Example: apps/myapp.
  """

  domainMapping = _messages.MessageField('DomainMapping', 1)
  noManagedCertificate = _messages.BooleanField(2)
  parent = _messages.StringField(3, required=True)


class AppengineAppsDomainMappingsDeleteRequest(_messages.Message):
  """A AppengineAppsDomainMappingsDeleteRequest object.

  Fields:
    name: Name of the resource to delete. Example:
      apps/myapp/domainMappings/example.com.
  """

  name = _messages.StringField(1, required=True)


class AppengineAppsDomainMappingsGetRequest(_messages.Message):
  """A AppengineAppsDomainMappingsGetRequest object.

  Fields:
    name: Name of the resource requested. Example:
      apps/myapp/domainMappings/example.com.
  """

  name = _messages.StringField(1, required=True)


class AppengineAppsDomainMappingsListRequest(_messages.Message):
  """A AppengineAppsDomainMappingsListRequest object.

  Fields:
    pageSize: Maximum results to return per page.
    pageToken: Continuation token for fetching the next page of results.
    parent: Name of the parent Application resource. Example: apps/myapp.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class AppengineAppsDomainMappingsPatchRequest(_messages.Message):
  """A AppengineAppsDomainMappingsPatchRequest object.

  Fields:
    domainMapping: A DomainMapping resource to be passed as the request body.
    name: Name of the resource to update. Example:
      apps/myapp/domainMappings/example.com.
    noManagedCertificate: Whether a managed certificate should be provided by
      App Engine. If true, a certificate ID must be manaually set in the
      DomainMapping resource to configure SSL for this domain. If false, a
      managed certificate will be provisioned and a certificate ID will be
      automatically populated. Only applicable if ssl_settings.certificate_id
      is specified in the update mask.
    updateMask: Standard field mask for the set of fields to be updated.
  """

  domainMapping = _messages.MessageField('DomainMapping', 1)
  name = _messages.StringField(2, required=True)
  noManagedCertificate = _messages.BooleanField(3)
  updateMask = _messages.StringField(4)


class AppengineAppsLocationsGetRequest(_messages.Message):
  """A AppengineAppsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class AppengineAppsLocationsListRequest(_messages.Message):
  """A AppengineAppsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class AppengineAppsOperationsGetRequest(_messages.Message):
  """A AppengineAppsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class AppengineAppsOperationsListRequest(_messages.Message):
  """A AppengineAppsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class AuthorizedCertificate(_messages.Message):
  """An SSL certificate that a user has been authorized to administer. A user
  is authorized to administer any certificate that applies to one of their
  authorized domains.

  Fields:
    certificateRawData: The SSL certificate serving the AuthorizedCertificate
      resource. This must be obtained independently from a certificate
      authority.
    displayName: The user-specified display name of the certificate. This is
      not guaranteed to be unique. Example: My Certificate.
    domainMappingsCount: Aggregate count of the domain mappings with this
      certificate mapped. This count includes domain mappings on applications
      for which the user does not have VIEWER permissions.Only returned by GET
      requests when specifically requested by the view=FULL option.@OutputOnly
    domainNames: Topmost applicable domains of this certificate. This
      certificate applies to these domains and their subdomains. Example:
      example.com.@OutputOnly
    expireTime: The time when this certificate expires. To update the renewal
      time on this certificate, upload an SSL certificate with a different
      expiration time using
      AuthorizedCertificates.UpdateAuthorizedCertificate.@OutputOnly
    id: Relative name of the certificate. This is a unique value autogenerated
      on AuthorizedCertificate resource creation. Example: 12345.@OutputOnly
    managedCertificate: Only applicable if this certificate is managed by App
      Engine. Managed certificates are tied to the lifecycle of a
      DomainMapping and cannot be updated or deleted via the
      AuthorizedCertificates API. If this certificate is manually administered
      by the user, this field will be empty.@OutputOnly
    name: Full path to the AuthorizedCertificate resource in the API. Example:
      apps/myapp/authorizedCertificates/12345.@OutputOnly
    visibleDomainMappings: The full paths to user visible Domain Mapping
      resources that have this certificate mapped. Example:
      apps/myapp/domainMappings/example.com.This may not represent the full
      list of mapped domain mappings if the user does not have VIEWER
      permissions on all of the applications that have this certificate
      mapped. See domain_mappings_count for a complete count.Only returned by
      GET requests when specifically requested by the view=FULL
      option.@OutputOnly
  """

  certificateRawData = _messages.MessageField('CertificateRawData', 1)
  displayName = _messages.StringField(2)
  domainMappingsCount = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  domainNames = _messages.StringField(4, repeated=True)
  expireTime = _messages.StringField(5)
  id = _messages.StringField(6)
  managedCertificate = _messages.MessageField('ManagedCertificate', 7)
  name = _messages.StringField(8)
  visibleDomainMappings = _messages.StringField(9, repeated=True)


class AuthorizedDomain(_messages.Message):
  """A domain that a user has been authorized to administer. To authorize use
  of a domain, verify ownership via Webmaster Central
  (https://www.google.com/webmasters/verification/home).

  Fields:
    id: Fully qualified domain name of the domain authorized for use. Example:
      example.com.
    name: Full path to the AuthorizedDomain resource in the API. Example:
      apps/myapp/authorizedDomains/example.com.@OutputOnly
  """

  id = _messages.StringField(1)
  name = _messages.StringField(2)


class CertificateRawData(_messages.Message):
  """An SSL certificate obtained from a certificate authority.

  Fields:
    privateKey: Unencrypted PEM encoded RSA private key. This field is set
      once on certificate creation and then encrypted. The key size must be
      2048 bits or fewer. Must include the header and footer. Example: <pre>
      -----BEGIN RSA PRIVATE KEY----- <unencrypted_key_value> -----END RSA
      PRIVATE KEY----- </pre> @InputOnly
    publicCertificate: PEM encoded x.509 public key certificate. This field is
      set once on certificate creation. Must include the header and footer.
      Example: <pre> -----BEGIN CERTIFICATE----- <certificate_value> -----END
      CERTIFICATE----- </pre>
  """

  privateKey = _messages.StringField(1)
  publicCertificate = _messages.StringField(2)


class DomainMapping(_messages.Message):
  """A domain serving an App Engine application.

  Fields:
    id: Relative name of the domain serving the application. Example:
      example.com.
    name: Full path to the DomainMapping resource in the API. Example:
      apps/myapp/domainMapping/example.com.@OutputOnly
    resourceRecords: The resource records required to configure this domain
      mapping. These records must be added to the domain's DNS configuration
      in order to serve the application via this domain mapping.@OutputOnly
    sslSettings: SSL configuration for this domain. If unconfigured, this
      domain will not serve with SSL.
  """

  id = _messages.StringField(1)
  name = _messages.StringField(2)
  resourceRecords = _messages.MessageField('ResourceRecord', 3, repeated=True)
  sslSettings = _messages.MessageField('SslSettings', 4)


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo {   rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); } The JSON
  representation for Empty is empty JSON object {}.
  """



class ListAuthorizedCertificatesResponse(_messages.Message):
  """Response message for AuthorizedCertificates.ListAuthorizedCertificates.

  Fields:
    certificates: The SSL certificates the user is authorized to administer.
    nextPageToken: Continuation token for fetching the next page of results.
  """

  certificates = _messages.MessageField('AuthorizedCertificate', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListAuthorizedDomainsResponse(_messages.Message):
  """Response message for AuthorizedDomains.ListAuthorizedDomains.

  Fields:
    domains: The authorized domains belonging to the user.
    nextPageToken: Continuation token for fetching the next page of results.
  """

  domains = _messages.MessageField('AuthorizedDomain', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListDomainMappingsResponse(_messages.Message):
  """Response message for DomainMappings.ListDomainMappings.

  Fields:
    domainMappings: The domain mappings for the application.
    nextPageToken: Continuation token for fetching the next page of results.
  """

  domainMappings = _messages.MessageField('DomainMapping', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListLocationsResponse(_messages.Message):
  """The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  """The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Location(_messages.Message):
  """A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: "us-east1".
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: "projects/example-project/locations/us-
      east1"
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  labels = _messages.MessageField('LabelsValue', 1)
  locationId = _messages.StringField(2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)


class LocationMetadata(_messages.Message):
  """Metadata for the given google.cloud.location.Location.

  Fields:
    flexibleEnvironmentAvailable: App Engine Flexible Environment is available
      in the given location.@OutputOnly
    standardEnvironmentAvailable: App Engine Standard Environment is available
      in the given location.@OutputOnly
  """

  flexibleEnvironmentAvailable = _messages.BooleanField(1)
  standardEnvironmentAvailable = _messages.BooleanField(2)


class ManagedCertificate(_messages.Message):
  """A certificate managed by App Engine.

  Enums:
    StatusValueValuesEnum: Status of certificate management. Refers to the
      most recent certificate acquisition or renewal attempt.@OutputOnly

  Fields:
    lastRenewalTime: Time at which the certificate was last renewed. The
      renewal process is fully managed. Certificate renewal will automatically
      occur before the certificate expires. Renewal errors can be tracked via
      ManagementStatus.@OutputOnly
    status: Status of certificate management. Refers to the most recent
      certificate acquisition or renewal attempt.@OutputOnly
  """

  class StatusValueValuesEnum(_messages.Enum):
    """Status of certificate management. Refers to the most recent certificate
    acquisition or renewal attempt.@OutputOnly

    Values:
      UNSPECIFIED_STATUS: <no description>
      OK: Certificate was successfully obtained and inserted into the serving
        system.
      PENDING: Certificate is under active attempts to acquire or renew.
      FAILED_RETRYING_INTERNAL: Most recent renewal failed due to a system
        failure and will be retried. System failure is likely transient, and
        subsequent renewal attempts may succeed. The last successfully
        provisioned certificate may still be serving.
      FAILED_RETRYING_NOT_VISIBLE: Most recent renewal failed due to an
        invalid DNS setup and will be retried. Renewal attempts will continue
        to fail until the certificate domain's DNS configuration is fixed. The
        last successfully provisioned certificate may still be serving.
      FAILED_PERMANENTLY_NOT_VISIBLE: All renewal attempts have been
        exhausted. Most recent renewal failed due to an invalid DNS setup and
        will not be retried. The last successfully provisioned certificate may
        still be serving.
    """
    UNSPECIFIED_STATUS = 0
    OK = 1
    PENDING = 2
    FAILED_RETRYING_INTERNAL = 3
    FAILED_RETRYING_NOT_VISIBLE = 4
    FAILED_PERMANENTLY_NOT_VISIBLE = 5

  lastRenewalTime = _messages.StringField(1)
  status = _messages.EnumField('StatusValueValuesEnum', 2)


class Operation(_messages.Message):
  """This resource represents a long-running operation that is the result of a
  network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success. If
      the original method returns no data on success, such as Delete, the
      response is google.protobuf.Empty. If the original method is standard
      Get/Create/Update, the response should be the resource. For other
      methods, the response should have the type XxxResponse, where Xxx is the
      original method name. For example, if the original method name is
      TakeSnapshot(), the inferred response type is TakeSnapshotResponse.

  Fields:
    done: If the value is false, it means the operation is still in progress.
      If true, the operation is completed, and either error or response is
      available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the name should have the format of operations/some/unique/name.
    response: The normal response of the operation in case of success. If the
      original method returns no data on success, such as Delete, the response
      is google.protobuf.Empty. If the original method is standard
      Get/Create/Update, the response should be the resource. For other
      methods, the response should have the type XxxResponse, where Xxx is the
      original method name. For example, if the original method name is
      TakeSnapshot(), the inferred response type is TakeSnapshotResponse.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    """The normal response of the operation in case of success. If the
    original method returns no data on success, such as Delete, the response
    is google.protobuf.Empty. If the original method is standard
    Get/Create/Update, the response should be the resource. For other methods,
    the response should have the type XxxResponse, where Xxx is the original
    method name. For example, if the original method name is TakeSnapshot(),
    the inferred response type is TakeSnapshotResponse.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadata(_messages.Message):
  """Metadata for the given google.longrunning.Operation.

  Fields:
    endTime: Timestamp that this operation completed.@OutputOnly
    insertTime: Timestamp that this operation was created.@OutputOnly
    method: API method that initiated this operation. Example:
      google.appengine.v1beta4.Version.CreateVersion.@OutputOnly
    operationType: Type of this operation. Deprecated, use method field
      instead. Example: "create_version".@OutputOnly
    target: Name of the resource that this operation is acting on. Example:
      apps/myapp/modules/default.@OutputOnly
    user: User who requested this operation.@OutputOnly
  """

  endTime = _messages.StringField(1)
  insertTime = _messages.StringField(2)
  method = _messages.StringField(3)
  operationType = _messages.StringField(4)
  target = _messages.StringField(5)
  user = _messages.StringField(6)


class OperationMetadataExperimental(_messages.Message):
  """Metadata for the given google.longrunning.Operation.

  Fields:
    endTime: Time that this operation completed.@OutputOnly
    insertTime: Time that this operation was created.@OutputOnly
    method: API method that initiated this operation. Example:
      google.appengine.experimental.CustomDomains.CreateCustomDomain.@OutputOn
      ly
    target: Name of the resource that this operation is acting on. Example:
      apps/myapp/customDomains/example.com.@OutputOnly
    user: User who requested this operation.@OutputOnly
  """

  endTime = _messages.StringField(1)
  insertTime = _messages.StringField(2)
  method = _messages.StringField(3)
  target = _messages.StringField(4)
  user = _messages.StringField(5)


class OperationMetadataV1(_messages.Message):
  """Metadata for the given google.longrunning.Operation.

  Fields:
    endTime: Time that this operation completed.@OutputOnly
    ephemeralMessage: Ephemeral message that may change every time the
      operation is polled. @OutputOnly
    insertTime: Time that this operation was created.@OutputOnly
    method: API method that initiated this operation. Example:
      google.appengine.v1.Versions.CreateVersion.@OutputOnly
    target: Name of the resource that this operation is acting on. Example:
      apps/myapp/services/default.@OutputOnly
    user: User who requested this operation.@OutputOnly
    warning: Durable messages that persist on every operation poll.
      @OutputOnly
  """

  endTime = _messages.StringField(1)
  ephemeralMessage = _messages.StringField(2)
  insertTime = _messages.StringField(3)
  method = _messages.StringField(4)
  target = _messages.StringField(5)
  user = _messages.StringField(6)
  warning = _messages.StringField(7, repeated=True)


class OperationMetadataV1Alpha(_messages.Message):
  """Metadata for the given google.longrunning.Operation.

  Fields:
    endTime: Time that this operation completed.@OutputOnly
    ephemeralMessage: Ephemeral message that may change every time the
      operation is polled. @OutputOnly
    insertTime: Time that this operation was created.@OutputOnly
    method: API method that initiated this operation. Example:
      google.appengine.v1alpha.Versions.CreateVersion.@OutputOnly
    target: Name of the resource that this operation is acting on. Example:
      apps/myapp/services/default.@OutputOnly
    user: User who requested this operation.@OutputOnly
    warning: Durable messages that persist on every operation poll.
      @OutputOnly
  """

  endTime = _messages.StringField(1)
  ephemeralMessage = _messages.StringField(2)
  insertTime = _messages.StringField(3)
  method = _messages.StringField(4)
  target = _messages.StringField(5)
  user = _messages.StringField(6)
  warning = _messages.StringField(7, repeated=True)


class OperationMetadataV1Beta(_messages.Message):
  """Metadata for the given google.longrunning.Operation.

  Fields:
    endTime: Time that this operation completed.@OutputOnly
    ephemeralMessage: Ephemeral message that may change every time the
      operation is polled. @OutputOnly
    insertTime: Time that this operation was created.@OutputOnly
    method: API method that initiated this operation. Example:
      google.appengine.v1beta.Versions.CreateVersion.@OutputOnly
    target: Name of the resource that this operation is acting on. Example:
      apps/myapp/services/default.@OutputOnly
    user: User who requested this operation.@OutputOnly
    warning: Durable messages that persist on every operation poll.
      @OutputOnly
  """

  endTime = _messages.StringField(1)
  ephemeralMessage = _messages.StringField(2)
  insertTime = _messages.StringField(3)
  method = _messages.StringField(4)
  target = _messages.StringField(5)
  user = _messages.StringField(6)
  warning = _messages.StringField(7, repeated=True)


class OperationMetadataV1Beta5(_messages.Message):
  """Metadata for the given google.longrunning.Operation.

  Fields:
    endTime: Timestamp that this operation completed.@OutputOnly
    insertTime: Timestamp that this operation was created.@OutputOnly
    method: API method name that initiated this operation. Example:
      google.appengine.v1beta5.Version.CreateVersion.@OutputOnly
    target: Name of the resource that this operation is acting on. Example:
      apps/myapp/services/default.@OutputOnly
    user: User who requested this operation.@OutputOnly
  """

  endTime = _messages.StringField(1)
  insertTime = _messages.StringField(2)
  method = _messages.StringField(3)
  target = _messages.StringField(4)
  user = _messages.StringField(5)


class ResourceRecord(_messages.Message):
  """A DNS resource record.

  Enums:
    TypeValueValuesEnum: Resource record type. Example: AAAA.

  Fields:
    name: Relative name of the object affected by this record. Only applicable
      for CNAME records. Example: 'www'.
    rrdata: Data for this record. Values vary by record type, as defined in
      RFC 1035 (section 5) and RFC 1034 (section 3.6.1).
    type: Resource record type. Example: AAAA.
  """

  class TypeValueValuesEnum(_messages.Enum):
    """Resource record type. Example: AAAA.

    Values:
      A: An A resource record. Data is an IPv4 address.
      AAAA: An AAAA resource record. Data is an IPv6 address.
      CNAME: A CNAME resource record. Data is a domain name to be aliased.
    """
    A = 0
    AAAA = 1
    CNAME = 2

  name = _messages.StringField(1)
  rrdata = _messages.StringField(2)
  type = _messages.EnumField('TypeValueValuesEnum', 3)


class SslSettings(_messages.Message):
  """SSL configuration for a DomainMapping resource.

  Fields:
    certificateId: ID of the AuthorizedCertificate resource configuring SSL
      for the application. Clearing this field will remove SSL support.By
      default, a managed certificate is automatically created for every domain
      mapping. To omit SSL support or to configure SSL manually, specify
      no_managed_certificate on a CREATE or UPDATE request. You must be
      authorized to administer the AuthorizedCertificate resource to manually
      map it to a DomainMapping resource. Example: 12345.
    isManagedCertificate: Whether the mapped certificate is an App Engine
      managed certificate. Managed certificates are created by default with a
      domain mapping. To opt out, specify no_managed_certificate on a CREATE
      or UPDATE request.@OutputOnly
  """

  certificateId = _messages.StringField(1)
  isManagedCertificate = _messages.BooleanField(2)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class Status(_messages.Message):
  """The Status type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by gRPC (https://github.com/grpc). The error model is designed to be:
  Simple to use and understand for most users Flexible enough to meet
  unexpected needsOverviewThe Status message contains three pieces of data:
  error code, error message, and error details. The error code should be an
  enum value of google.rpc.Code, but it may accept additional error codes if
  needed. The error message should be a developer-facing English message that
  helps developers understand and resolve the error. If a localized user-
  facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package google.rpc that can be used for common error
  conditions.Language mappingThe Status message is the logical representation
  of the error model, but it is not necessarily the actual wire format. When
  the Status message is exposed in different client libraries and different
  wire protocols, it can be mapped differently. For example, it will likely be
  mapped to some exceptions in Java, but more likely mapped to some error
  codes in C.Other usesThe error model and the Status message can be used in a
  variety of environments, either with or without APIs, to provide a
  consistent developer experience across different environments.Example uses
  of this error model include: Partial errors. If a service needs to return
  partial errors to the client, it may embed the Status in the normal response
  to indicate the partial errors. Workflow errors. A typical workflow has
  multiple steps. Each step may have a Status message for error reporting.
  Batch operations. If a client uses batch request and batch response, the
  Status message should be used directly inside batch response, one for each
  error sub-response. Asynchronous operations. If an API call embeds
  asynchronous operation results in its response, the status of those
  operations should be represented directly using the Status message. Logging.
  If some API errors are stored in logs, the message Status could be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There will be a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'appengine')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'appengine')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'appengine')
