# ! / usr / bin / python
#by daniel reyes manuel :V

clase  S ( BaseHTTPRequestHandler ):
    def  _set_headers ( self ):
        auto .send_response ( 200 )
        self .send_header ( ' Content-type ' , ' text / html ' )
        self .end_headers ()

    def  do_GET ( self ):
        self ._set_headers ()
        self .wfile.write ( " <html> <cuerpo> <h1> hi! </ h1> </ body> </ html> " )

    def  do_HEAD ( self ):
        self ._set_headers ()
        
    def  do_POST ( self ):
        self ._set_headers ()
        self .wfile.write ( " <html> <cuerpo> <h1> POST! </ h1> </ body> </ html> " )
        
def  run ( server_class = HTTPServer, handler_class = S, port = 80 ):
    server_address = ( ' ' , puerto)
    httpd = server_class (server_address, handler_class)
    imprimir  ' Iniciando httpd ... '
    httpd.serve_forever ()

si  __name__  ==  " __main__ " :
    de sys import argv

    si  len (argv) ==  2 :
        ejecutar ( port = int (argv [ 1 ]))
    else :
        correr()