from ssl import SSLContext, CERT_REQUIRED, PROTOCOL_TLSv1_2, OP_NO_COMPRESSION, \
    OP_SINGLE_ECDH_USE, OP_CIPHER_SERVER_PREFERENCE
from config_main import ca_crt, server_key, server_crt

context = SSLContext(PROTOCOL_TLSv1_2)
context.set_ecdh_curve('prime256v1')
context.verify_mode = CERT_REQUIRED
context.set_ciphers('ECDHE-RSA-AES256-GCM-SHA384')
context.options |= OP_NO_COMPRESSION
context.options |= OP_SINGLE_ECDH_USE
context.options |= OP_CIPHER_SERVER_PREFERENCE
context.load_verify_locations(ca_crt)
context.load_cert_chain(server_crt, server_key)
