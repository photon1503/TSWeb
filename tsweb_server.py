from waitress import serve
import tsweb
serve(tsweb.app, host='0.0.0.0', port=8081)