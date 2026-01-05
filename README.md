# Plataforma de Validación Automatizada CI/CD

## What is this?

Proyecto **simple y directo** que demuestra cómo diseñar un **pipeline de CI/CD** para validar automáticamente software, inspirado en flujos reales de **validación de software de vehículo / infotainment**.

Cada cambio de código se prueba automáticamente usando **tests en Python**, bloqueando errores antes de integrarlos.

---

## Skills demostrados

* Integración Continua (CI) con **GitHub Actions**
* Automatización de tests en **Python (pytest)**
* Validación automática en cada commit
* Buenas prácticas con **Git**
* Enfoque *shift-left testing*

---

## 🧱 Estructura

```
├── app/        # Servicio simulado de infotainment
├── tests/      # Tests automatizados en Python
├── scripts/    # Smoke tests
├── .github/    # Pipeline CI/CD
└── Dockerfile  # Opcional
```

---

## Validación automática

* Test de disponibilidad del servicio
* Validación de respuesta y estado
* Smoke test rápido en Bash

Los tests se ejecutan:

* En local
* Automáticamente en el pipeline CI

Si un test falla → el cambio no pasa.

---

## Pipeline CI/CD

El pipeline:

1. Descarga el código
2. Configura Python
3. Arranca la aplicación
4. Ejecuta los tests
5. Falla si algo no es válido

Esto garantiza **calidad continua**.

---

## ▶️ Ejecutar en local

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask requests pytest
python app/main.py
pytest tests/
```

---

## Por qué existe

Simular un entorno real donde:

* El software se valida automáticamente
* Los errores se detectan pronto
* La calidad es parte del pipeline, no un paso manual

---

## Próximos pasos

* Jenkins / Bamboo
* Más tests automáticos
* Despliegue en Kubernetes (K3s)
* Integración con AWS

---

