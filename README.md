# jwt_crack 

This Python script attempts to brute-force the secret key used to sign a JSON Web Token (JWT) that uses the HS256 algorithm. It works by trying each key from a user-supplied wordlist until it finds a matching signature.

## Usage
`pip install PyJWT`

`python jwt_cracker.py <jwt_token> list.txt`

Test with the default jwt from jwt.io: `python jwt_crack.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30 list.txt`

```
$ ./jwt_crack.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30 list.txt
[+] Secret found: 'a-string-secret-at-least-256-bits-long'
[+] Payload: {'sub': '1234567890', 'name': 'John Doe', 'admin': True, 'iat': 1516239022}
```

Wordlist from [https://github.com/wallarm/jwt-secrets](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list).