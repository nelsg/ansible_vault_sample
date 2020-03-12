# Vault usage sample with scripts

Ce playbooks est un exemple d'utilisation plus complète que ce que l'on peut penser utiliser au premier abord. Cette méthode permet d'avoir plusieurs vaults avec chacun son mot de passe voir quelques uns qui peuvent se partager le même mot de passe à travers la clé `my_key_1` ou `my_key_2`.

La variable `vault_id_match` fait un matching strict sur les clés de vaults, il utilise le mot de passe correspondant à la clé. Par défault ansible teste tous les mots de passes avec tous les vaults.

Mots de passes à utiliser :

* password 1 : **pwd1**
* password 2 : **pwd2**


## Commands

Encrypt a string with vault 1 :

```
echo -n 'Hello' | ansible-vault encrypt_string --vault-id my_key_1@prompt --stdin-name 'my_value_1'
echo -n 'World' | ansible-vault encrypt_string --vault-id my_key_2@prompt --stdin-name 'my_value_2'
```

> Not works on MacOS and Windows, `keyctl` only available on Linux
