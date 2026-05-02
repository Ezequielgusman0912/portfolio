from django.shortcuts import render


def home(request):
    context = {
        "profile": {
            "name": "Ezequiel Gusman",
            "role": "Analista Funcional & Backend Developer",
            "location": "Cordoba, Argentina",
            "email": "ezeegus35@gmail.com",
            "phone": "+54 351 7645672",
            "linkedin": "https://www.linkedin.com/in/ezequiel-gusman-",
            "summary": (
                "Estudiante avanzado de Ingenieria en Sistemas con foco en "
                "backend, analisis funcional e infraestructura cloud. Trabajo "
                "con Python, Django, Azure e integraciones IoT en tiempo real."
            ),
        },
        "highlights": [
            "Backend con Python/Django y Django REST Framework",
            "Despliegues cloud en Azure App Service con MSAL",
            "WebSockets e integraciones con Raspberry Pi para monitoreo IoT",
            "Observabilidad con Grafana, Scrum, Jira y Azure DevOps",
        ],
        "experiences": [
            {
                "company": "Porta Hnos. S.A.",
                "role": "Desarrollador Backend",
                "period": "Julio 2025 - Actualidad",
                "description": (
                    "Diseno y escalabilidad de arquitectura server-side, "
                    "transicion hacia microservicios y servicios cloud."
                ),
                "items": [
                    "Desarrollo y mantenimiento de servicios con Python y Django.",
                    "Configuracion de Azure App Service, MSAL y bases MySQL.",
                    "Comunicacion bidireccional con WebSockets y Raspberry Pi.",
                    "Tableros Grafana para metricas y salud de sistemas.",
                ],
            },
            {
                "company": "Porta Hnos. S.A.",
                "role": "Analista de Sistemas IT",
                "period": "Febrero 2025 - Julio 2025",
                "description": (
                    "Nexo entre usuarios finales y desarrollo para el ERP "
                    "corporativo, con foco en requerimientos, bugs y backlog."
                ),
                "items": [
                    "Relevamiento de requerimientos funcionales.",
                    "Diagnostico de bugs y documentacion tecnica.",
                    "Analisis de datos con consultas directas al ERP.",
                ],
            },
            {
                "company": "Porta Hnos. S.A.",
                "role": "Pasante de IT",
                "period": "Abril 2024 - Febrero 2025",
                "description": (
                    "Soporte tecnico y administracion de sistemas en entornos "
                    "industriales y productivos."
                ),
                "items": [
                    "Administracion de usuarios y permisos en Active Directory.",
                    "Soporte funcional a ERP, WMS y SharePoint.",
                ],
            },
        ],
        "skills": {
            "Lenguajes": ["Python", "JavaScript", "HTML/CSS", "SQL", "Ruby"],
            "Backend": ["Django", "Django REST Framework", "MySQL", "WebSockets"],
            "Cloud y herramientas": ["Azure App Service", "MSAL", "Grafana", "Git", "Azure DevOps"],
            "Producto y gestion": ["Scrum", "Agile", "Analisis Funcional", "Jira", "Confluence"],
        },
        "education": [
            "Ingenieria en Sistemas de Informacion - UTN FRC, cursando 3er ano",
            "Bachiller con orientacion en Turismo - Escuela Nro 122 Dr. Roberto Beracochea",
        ],
        "certifications": [
            "Python Avanzado - EducacionIT (2025)",
            "Introduccion a Python - EducacionIT (2025)",
            "MySQL Esencial - LinkedIn Learning (2022)",
            "Fundamentos de Desarrollo Web Full Stack - LinkedIn Learning (2022)",
            "Scrum y Metodologias Agiles - EducacionIT",
        ],
        "projects": [
            {
                "name": "Monitoreo IoT en tiempo real",
                "description": (
                    "Integracion backend con dispositivos Raspberry Pi mediante "
                    "WebSockets para seguimiento de hardware en tiempo real."
                ),
                "tags": ["Python", "Django", "WebSockets", "IoT"],
            },
            {
                "name": "Servicios cloud internos",
                "description": (
                    "Microservicios y despliegues en Azure App Service con "
                    "autenticacion MSAL y persistencia MySQL."
                ),
                "tags": ["Azure", "MSAL", "MySQL", "Django"],
            },
            {
                "name": "Observabilidad operativa",
                "description": (
                    "Tableros de Grafana para visualizar metricas criticas, "
                    "estado de servicios y salud del sistema."
                ),
                "tags": ["Grafana", "Metrica", "DevOps"],
            },
        ],
    }
    return render(request, "portfolio/home.html", context)
