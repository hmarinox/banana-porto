import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
	http.get('http://localhost:8000/visitor');
	http.get('http://localhost:8000/500');
	http.get('http://localhost:8000/404');
	http.get('http://localhost:8000/divbyzero');
	sleep(1);
}
