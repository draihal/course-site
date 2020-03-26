import jwtDecode from 'jwt-decode';


export class AuthToken {
    constructor(token) {
        this.token = token;
        this.decodedToken = { user_id: '', exp: 0 };
        try {
            if (token)
                this.decodedToken = jwtDecode(token);
        }
        catch (e) { }
    }
    get expiresAt() {
        return new Date(this.decodedToken.exp * 1000);  // 'exp':1580165326
    }
    get isExpired() {
        return new Date() > this.expiresAt;
    }
    get isAuthenticated() {
        return !this.isExpired;
    }
    get authorizationString() {
        return `JWT ${this.token}`;
    }
}
