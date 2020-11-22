import http from 'k6/http';
import { sleep } from 'k6';

export visitor function () {
	http.get('http://localhost:8000/visitor');
	sleep(1);
}
export http500 function () {
	http.get('http://localhost:8000/visitor');
	http.get('http://localhost:8000/500');
	http.get('http://localhost:8000/404');
	http.get('http://localhost:8000/divbyzero');
	sleep(1);
}
