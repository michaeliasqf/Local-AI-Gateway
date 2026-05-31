#Local AI Gateway

Un gateway ligero en FastAPI para exponer modelos de IA locales (Ollama) como una API tipo cloud, permitiendo consumir inferencia desde cualquier dispositivo dentro de la red.

##🚀 Por qué existe este proyecto

El uso de modelos de IA vía APIs cloud (OpenAI, Anthropic, etc.) está creciendo rápidamente en entornos empresariales, pero trae dos problemas cada vez más relevantes:

**💸 Costo creciente por consumo de tokens**
**🔐 Dependencia y exposición de datos sensibles en infraestructura externa**

Muchas organizaciones están empezando a evaluar un cambio hacia infraestructura de IA local o híbrida, donde el control de datos, latencia y costos sea administrado internamente.

Este proyecto nace como una base práctica para ese enfoque:

Un gateway simple que permite convertir un modelo local en un servicio tipo API consumible desde cualquier dispositivo en la red.

##🧠 Qué es este proyecto

Este sistema es una capa intermedia entre:

🧩 Ollama (motor de modelos locales)
🌐 Clientes externos (web, móvil, apps internas)

y expone una API limpia tipo:

POST /generate
🏗️ Arquitectura
Cliente (móvil / PC / app)
        ↓
FastAPI Gateway
        ↓
Ollama API (local)
        ↓
Modelo LLM (ej: gemma, llama, mistral)

##⚙️ Características
✔ API REST simple y extensible
✔ Compatible con cualquier modelo de Ollama
✔ Medición de latencia por request
✔ Preparado para red local (LAN)
✔ Fácil de extender a producción (auth, logs, rate limiting)

##📦 Instalación
1. Clonar repo
git clone https://github.com/tuusuario/local-ai-gateway.git
cd local-ai-gateway
2. Instalar dependencias
pip install fastapi uvicorn requests
3. Instalar Ollama

Descargar desde:
https://ollama.com

Ejemplo de modelo:
ollama run gemma4:e4b

##▶️ Ejecución
Levantar el gateway:
uvicorn main:app --host 0.0.0.0 --port 8000

Esto permite acceso desde otros dispositivos en la red.

📡 Uso de la API
Health check
GET /health

Respuesta:

{
  "status": "ok"
}
Generación de texto
POST /generate
Content-Type: application/json
{
  "prompt": "Explícame qué es un modelo de lenguaje",
  "model": "gemma4:e4b"
}
Respuesta
{
  "response": "Un modelo de lenguaje es...",
  "model": "gemma4:e4b",
  "latency_sec": 1.42
}

##🔧 Casos de uso
🏢 Empresas que quieren IA interna sin exponer datos sensibles
📱 Apps móviles conectadas a IA local
🧪 Prototipos de asistentes privados
🖥️ Laboratorios de IA con control total del entorno
💰 Reducción de costos en inferencia cloud
📈 Por qué esto es relevante hoy

La tendencia actual en IA muestra:

**Incremento sostenido en consumo de tokens**
**Mayor uso de modelos en producción (no solo testing)**
**Necesidad de control de datos internos**
**Migración parcial a modelos locales o híbridos**

Este tipo de gateway es el primer paso hacia una arquitectura de IA:

Private-first, cost-controlled AI infrastructure

##🔒 Seguridad (recomendado)
Actualmente el proyecto es para red local.
Para entornos productivos se recomienda agregar:

Autenticación JWT
Rate limiting
Logging centralizado
HTTPS (reverse proxy con Nginx)
Control de acceso por IP

##🧩 Extensiones posibles
Streaming de tokens (tipo ChatGPT)
Soporte multi-modelo con routing automático
Cache de respuestas frecuentes
Panel web de monitoreo
Cola de requests con Redis
OpenAI-compatible API layer

##📌 Tecnologías
FastAPI
Ollama
Python 3.10+
HTTPX / Requests
