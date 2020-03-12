# Vault usage sample with scripts

password 1 is : pwd1
password 2 is : pwd2


## Commands

Encrypt a string with vault 1 :

```
echo -n 'Hello' | ansible-vault encrypt_string --vault-id my_key_1@prompt --stdin-name 'my_value_1'
echo -n 'World' | ansible-vault encrypt_string --vault-id my_key_2@prompt --stdin-name 'my_value_2'
```

> Not works on MacOS and Windows, `keyctl` only available on Linux
