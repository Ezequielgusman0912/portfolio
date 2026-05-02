from django.shortcuts import render


PROFILE = {
    "name": "Ezequiel Gusman",
    "role": "Analista Funcional & Backend Developer",
    "location": "Cordoba, Argentina",
    "email": "ezeegus35@gmail.com",
    "phone": "+54 351 7645672",
    "linkedin": "https://www.linkedin.com/in/ezequiel-gusman-",
    "summary": (
        "Estudiante avanzado de Ingenieria en Sistemas con foco en backend, "
        "analisis funcional e infraestructura cloud. Desarrollo ecosistemas "
        "con Python, Django, Azure, MySQL, WebSockets e integraciones IoT "
        "para flujos de datos de alta disponibilidad."
    ),
}

HIGHLIGHTS = [
    "Microservicios con Python, Django y Django REST Framework",
    "Azure App Service, MSAL, MySQL y despliegues automatizados",
    "WebSockets con Raspberry Pi para monitoreo y control IoT",
    "Grafana, Jira, Confluence, Scrum y Azure DevOps",
]

TECH_BADGES = [
    {
        "name": "Python",
        "label": "Backend scripting",
        "icon": "python",
    },
    {
        "name": "Django",
        "label": "Web apps y APIs",
        "icon": "django",
    },
    {
        "name": "MySQL",
        "label": "Datos relacionales",
        "icon": "mysql",
    },
]

EXPERIENCES = [
    {
        "company": "Porta Hnos. S.A.",
        "role": "Desarrollador Backend",
        "period": "Julio 2025 - Actualidad / Jornada completa / Hibrido",
        "description": (
            "Participo en el diseno y escalabilidad de arquitectura server-side, "
            "aportando a soluciones core de la compania e integraciones con "
            "plataformas de terceros. Mi foco esta en servicios cloud, "
            "microservicios y flujos de datos de alta disponibilidad."
        ),
        "items": [
            "Diseno y mantenimiento de microservicios con Python, Django y Django REST Framework.",
            "Backends para consumo y exposicion de datos hacia servicios internos y externos.",
            "Gestion de aplicaciones en Azure App Service con autenticacion corporativa mediante MSAL.",
            "Administracion de arquitecturas de datos en MySQL.",
            "Comunicacion bidireccional con WebSockets para hardware distribuido en Raspberry Pi.",
            "Tableros avanzados en Grafana para salud del sistema, metricas e integraciones.",
            "Pipelines en Azure DevOps y trabajo Scrum con Jira y Confluence.",
        ],
    },
    {
        "company": "Porta Hnos. S.A.",
        "role": "Analista de Sistemas IT",
        "period": "Febrero 2025 - Julio 2025 / Jornada completa / Hibrido",
        "description": (
            "Participe en el analisis funcional y mejora de sistemas internos "
            "integrados al ERP corporativo, actuando como nexo entre usuarios "
            "y el equipo de desarrollo."
        ),
        "items": [
            "Relevamiento de requerimientos, deteccion de mejoras y analisis de bugs.",
            "Gestion y seguimiento de incidencias mediante Jira.",
            "Documentacion de tareas y criterios tecnicos para desarrollo.",
            "Creacion y mantenimiento de tableros Grafana para metricas operativas.",
            "Consultas y analisis de datos en bases del ERP corporativo.",
            "Participacion en proyectos con Azure DevOps para tareas y versionado.",
            "Soporte a usuarios y resolucion de incidentes de infraestructura IT.",
        ],
    },
    {
        "company": "Porta Hnos. S.A.",
        "role": "Pasante de IT",
        "period": "Abril 2024 - Febrero 2025 / Jornada parcial / Presencial",
        "description": (
            "Brinde soporte tecnico a usuarios y colabore en la administracion "
            "de sistemas corporativos usados en entornos productivos e industriales."
        ),
        "items": [
            "Soporte tecnico a equipos, impresoras, dispositivos moviles y perifericos.",
            "Administracion basica de usuarios y permisos en Active Directory.",
            "Soporte funcional a ERP, WMS, SharePoint y WinCC.",
            "Diagnostico y resolucion de incidencias reportadas por usuarios internos.",
            "Instalacion y configuracion de software y hardware en estaciones de trabajo.",
            "Asistencia tecnica en entornos de oficina y produccion.",
        ],
    },
]

SKILLS = {
    "Lenguajes": ["Python", "JavaScript", "HTML/CSS", "SQL", "Ruby"],
    "Backend": ["Django", "Django REST Framework", "Microservicios", "WebSockets", "APIs"],
    "Datos y cloud": ["MySQL", "Azure App Service", "MSAL", "Grafana", "IoT"],
    "Herramientas": ["Git", "Azure DevOps", "Jira", "Confluence", "Active Directory"],
    "Producto y soporte": ["Scrum", "Agile", "Analisis Funcional", "ERP", "WMS", "WinCC"],
}

EDUCATION = [
    "Ingenieria en Sistemas de Informacion - UTN FRC, cursando 3er ano",
    "Bachiller con orientacion en Turismo - Escuela Nro 122 Dr. Roberto Beracochea",
]

CERTIFICATIONS = [
    "Python Avanzado - EducacionIT (2025)",
    "Introduccion a Python - EducacionIT (2025)",
    "MySQL Esencial - LinkedIn Learning (2022)",
    "Fundamentos de Desarrollo Web Full Stack - LinkedIn Learning (2022)",
    "Scrum y Metodologias Agiles - EducacionIT",
]

PROJECTS = [
    {
        "name": "Monitoreo IoT en tiempo real",
        "description": (
            "Integracion backend con dispositivos Raspberry Pi mediante WebSockets "
            "para seguimiento, monitoreo y control de hardware en tiempo real."
        ),
        "tags": ["Python", "Django", "WebSockets", "IoT"],
    },
    {
        "name": "Servicios cloud internos",
        "description": (
            "Microservicios y despliegues en Azure App Service con autenticacion "
            "MSAL, persistencia MySQL e integracion con plataformas de terceros."
        ),
        "tags": ["Azure", "MSAL", "MySQL", "Django"],
    },
    {
        "name": "Observabilidad operativa",
        "description": (
            "Tableros de Grafana para visualizar metricas criticas, estado de "
            "servicios, integraciones y salud del sistema."
        ),
        "tags": ["Grafana", "Metricas", "DevOps"],
    },
]


def base_context(active):
    return {
        "active": active,
        "profile": PROFILE,
    }


def home(request):
    context = base_context("home") | {
        "highlights": HIGHLIGHTS,
        "tech_badges": TECH_BADGES,
    }
    return render(request, "portfolio/home.html", context)


def experience(request):
    context = base_context("experience") | {
        "experiences": EXPERIENCES,
    }
    return render(request, "portfolio/experience.html", context)


def projects(request):
    context = base_context("projects") | {
        "projects": PROJECTS,
    }
    return render(request, "portfolio/projects.html", context)


def stack(request):
    context = base_context("stack") | {
        "skills": SKILLS,
        "tech_badges": TECH_BADGES,
        "education": EDUCATION,
        "certifications": CERTIFICATIONS,
    }
    return render(request, "portfolio/stack.html", context)


def contact(request):
    context = base_context("contact")
    return render(request, "portfolio/contact.html", context)
