import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';

import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class LoginService {

    private loginURL = 'http://localhost:8000/login/';
    datos_usuario = {};

    constructor(private http: Http) { }

    login(usuario:string, password:string): Observable<any>{
        return this.http
            .get(this.loginURL+'?usuario='+usuario+'&password='+password)
            .map((res: Response) => {
                res.json();
                this.datos_usuario = res.json();
            })
            .catch((error: any) => Observable.throw(error || 'Server error'));
    }

    getDatosUsuario() {
        return this.datos_usuario;
    }
}