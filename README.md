# CI/CD Python Test Automation

## Descripción

Repositorio de ejemplo que muestra cómo **validar software de forma automática** mediante un **pipeline de CI/CD**, usando Python y GitHub Actions.

La idea es simular un flujo real de validación como los que se usan en entornos industriales / infotainment, integrando **calidad y testing directamente en el pipeline**.

---

## Objetivo

* Ejecutar validaciones automáticas en cada commit
* Detectar errores lo antes posible (*shift-left testing*)
* Garantizar que solo el código válido se integra

---

## Estructura del proyecto

```
├── app/                 # Servicio simulado en Python
│   └── main.py
│
├── tests/
│   ├── unit/            # Tests rápidos
│   ├── integration/     # Tests de integración
│   └── performance/     # Validaciones básicas de rendimiento
│
├── scripts/             # Automatización y smoke tests
│   └── smoke_test.sh
│
├── .github/workflows/   # Pipeline CI/CD
│   └── ci.yml
│
├── Dockerfile           # Contenerización opcional
└── README.md
```

---

## Aplicación simulada

Servicio sencillo en **Python (Flask)** que expone un endpoint de salud:

```
GET /health
```

Respuesta esperada:

```json
{
  "status": "OK",
  "module": "infotainment"
}
```

El foco del proyecto no es la lógica de negocio, sino la **validación automática**.

---

## Estrategia de validación

La validación está estructurada por niveles:

* **Tests unitarios**: validaciones rápidas
* **Tests de integración**: validan el servicio en ejecución
* **Tests de rendimiento**: comprobaciones básicas de tiempo de respuesta
* **Smoke test**: validación rápida post-arranque

Este enfoque permite obtener **feedback rápido** y bloquear cambios no válidos.

---

## Pipeline CI/CD

El pipeline (GitHub Actions) ejecuta:

1. Checkout del código
2. Configuración del entorno Python
3. Instalación de dependencias
4. Arranque del servicio
5. Ejecución de tests por fases
6. Generación de reporte de resultados

Si alguna validación falla, el pipeline falla.

---

## Ejecutar en local

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask requests pytest
python app/main.py
```

En otra terminal:

```bash
pytest tests/
```

---

## Ejecutar con Docker

```bash
docker build -t ci-cd-validation .
docker run -d -p 5000:5000 ci-cd-validation
```

Tests dentro del contenedor:

```bash
docker exec -it <container_id> pytest tests/
```

---

##  Conceptos clave

* Integración Continua (CI/CD)
* Automatización de tests en Python
* Validación por fases
* Git y buenas prácticas
* Entornos reproducibles

---

