--- node.gypi.orig	2024-10-03 09:20:53 UTC
+++ node.gypi
@@ -354,6 +354,9 @@
     [ 'node_use_openssl=="true"', {
       'defines': [ 'HAVE_OPENSSL=1' ],
       'conditions': [
+        ['openssl_no_asm==1', {
+          'defines': [ 'OPENSSL_NO_ASM' ],
+        }],
         [ 'node_shared_openssl=="false"', {
           'defines': [ 'OPENSSL_API_COMPAT=0x10100000L', ],
           'dependencies': [
