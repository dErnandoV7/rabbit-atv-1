"# RabbitMQ - Atividade 1

Exemplo básico de comunicação com RabbitMQ usando Python.

## O que faz

- `send.py`: Envia mensagem "Hello World!" para uma fila
- `receive.py`: Recebe e exibe mensagens da fila
- `requirements.tx`: Lista a dependência `pika`

## Como usar

1. **Instalar RabbitMQ**

2. **Instalar dependências**:
   ```cmd
   python -m pip install pika --upgrade
   ```

   ```cmd
   # Terminal 1:
   python receive.py
   
   # Terminal 2: 
   python send.py
   ```

## Resultado

O `receive.py` fica aguardando mensagens e quando você roda o `send.py`, a mensagem aparece no primeiro terminal.

**Terminal 1:**
```
> Esperandno por mais mensagens.
[x] Received b'Hello World!'
```

**Terminal 2:**
```
[x] Sent 'Hello World!'
```" 
