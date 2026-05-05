# 14 Days to Building AI Systems & Agents

Este repositorio contiene los laboratorios prácticos del curso de 14 días.

## Configuración
1. Activar el entorno virtual: `.venv\Scripts\activate`
2. Instalar dependencias (se agregarán en el Día 3).

## Ejecución

Para probar el primer script:

python scripts/hello_ai.py

## Day 3: CLI Assistant

Create a `.env` file in the project root:

GROQ_API_KEY=your_key_here

Install dependencies:
pip install -r requirements.txt

Run:
python scripts/cli_assistant.py

## Day 4: Prompt Engineering
   
   Se ha creado una librería de prompts robustos en la carpeta `prompts/`.
   
   ### Plantillas incluidas:
   1. Resumidor Estructurado
   2. Extractor de Información
   3. Clasificador con Justificación
   4. Redactor Profesional
   5. Planificador de Pasos
   
   Cada plantilla incluye guardrails para evitar alucinaciones y asegurar la consistencia.