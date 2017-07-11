"""Generated message classes for oslogin version v1alpha.

A Google Cloud API for managing OS login configuration for Directory API
users.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'oslogin'


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class ImportSshPublicKeyResponse(_messages.Message):
  """A response message for importing an SSH public key.

  Fields:
    loginProfile: The login profile information for the user.
  """

  loginProfile = _messages.MessageField('LoginProfile', 1)


class LoginProfile(_messages.Message):
  """The Directory API profile information used for logging in to a virtual
  machine on Google Compute Engine.

  Messages:
    SshPublicKeysValue: A map from SSH public key fingerprint to the
      associated key object.

  Fields:
    name: A unique user ID for identifying the user.
    posixAccounts: The list of POSIX accounts associated with the Directory
      API user.
    sshPublicKeys: A map from SSH public key fingerprint to the associated key
      object.
    suspended: Indicates if the user is suspended.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class SshPublicKeysValue(_messages.Message):
    """A map from SSH public key fingerprint to the associated key object.

    Messages:
      AdditionalProperty: An additional property for a SshPublicKeysValue
        object.

    Fields:
      additionalProperties: Additional properties of type SshPublicKeysValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a SshPublicKeysValue object.

      Fields:
        key: Name of the additional property.
        value: A SshPublicKey attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('SshPublicKey', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  name = _messages.StringField(1)
  posixAccounts = _messages.MessageField('PosixAccount', 2, repeated=True)
  sshPublicKeys = _messages.MessageField('SshPublicKeysValue', 3)
  suspended = _messages.BooleanField(4)


class OsloginUsersGetLoginProfileRequest(_messages.Message):
  """A OsloginUsersGetLoginProfileRequest object.

  Fields:
    name: The unique ID for the user in format `users/{user}`.
  """

  name = _messages.StringField(1, required=True)


class OsloginUsersImportSshPublicKeyRequest(_messages.Message):
  """A OsloginUsersImportSshPublicKeyRequest object.

  Fields:
    parent: The unique ID for the user in format `users/{user}`.
    sshPublicKey: A SshPublicKey resource to be passed as the request body.
  """

  parent = _messages.StringField(1, required=True)
  sshPublicKey = _messages.MessageField('SshPublicKey', 2)


class OsloginUsersSshPublicKeysDeleteRequest(_messages.Message):
  """A OsloginUsersSshPublicKeysDeleteRequest object.

  Fields:
    name: The fingerprint of the public key to update. Public keys are
      identified by their SHA-256 fingerprint. The fingerprint of the public
      key is in format `users/{user}/sshPublicKeys/{fingerprint}`.
  """

  name = _messages.StringField(1, required=True)


class OsloginUsersSshPublicKeysGetRequest(_messages.Message):
  """A OsloginUsersSshPublicKeysGetRequest object.

  Fields:
    name: The fingerprint of the public key to retrieve. Public keys are
      identified by their SHA-256 fingerprint. The fingerprint of the public
      key is in format `users/{user}/sshPublicKeys/{fingerprint}`.
  """

  name = _messages.StringField(1, required=True)


class OsloginUsersSshPublicKeysPatchRequest(_messages.Message):
  """A OsloginUsersSshPublicKeysPatchRequest object.

  Fields:
    name: The fingerprint of the public key to update. Public keys are
      identified by their SHA-256 fingerprint. The fingerprint of the public
      key is in format `users/{user}/sshPublicKeys/{fingerprint}`.
    sshPublicKey: A SshPublicKey resource to be passed as the request body.
    updateMask: Mask to control which fields get updated. Updates all if not
      present.
  """

  name = _messages.StringField(1, required=True)
  sshPublicKey = _messages.MessageField('SshPublicKey', 2)
  updateMask = _messages.StringField(3)


class PosixAccount(_messages.Message):
  """The POSIX account information associated with a Directory API User.

  Fields:
    gecos: The GECOS (user information) entry for this account.
    gid: The default group ID.
    homeDirectory: The path to the home directory for this account.
    primary: Only one POSIX account can be marked as primary.
    shell: The path to the logic shell for this account.
    systemId: System identifier for which account the username or uid applies
      to. By default, the empty value is used.
    uid: The user ID.
    username: The username of the POSIX account.
  """

  gecos = _messages.StringField(1)
  gid = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  homeDirectory = _messages.StringField(3)
  primary = _messages.BooleanField(4)
  shell = _messages.StringField(5)
  systemId = _messages.StringField(6)
  uid = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  username = _messages.StringField(8)


class SshPublicKey(_messages.Message):
  """The SSH public key information associated with a Directory API User.

  Fields:
    expirationTimeUsec: An expiration time in microseconds since epoch.
    fingerprint: [Output Only] The SHA-256 fingerprint of the SSH public key.
    key: Public key text in SSH format, defined by <a
      href="https://www.ietf.org/rfc/rfc4253.txt" target="_blank">RFC4253</a>
      section 6.6.
  """

  expirationTimeUsec = _messages.IntegerField(1)
  fingerprint = _messages.StringField(2)
  key = _messages.StringField(3)


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


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'oslogin')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'oslogin')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'oslogin')
