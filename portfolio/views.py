from django.http import Http404
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
        "id": "backend-porta",
        "badge": "PH",
        "company": "Porta Hnos. S.A.",
        "role": "Desarrollador Backend",
        "from_to": "Jul. 2025 - Actualidad",
        "mode": "Jornada completa / Hibrido",
        "location": "Cordoba, Argentina",
        "summary": "Arquitectura backend, microservicios, Azure, integraciones y datos en tiempo real.",
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
        "id": "analista-porta",
        "badge": "PH",
        "company": "Porta Hnos. S.A.",
        "role": "Analista de Sistemas IT",
        "from_to": "Feb. 2025 - Jul. 2025",
        "mode": "Jornada completa / Hibrido",
        "location": "Cordoba, Argentina",
        "summary": "Analisis funcional, ERP corporativo, Jira, Grafana y soporte a usuarios.",
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
        "id": "pasante-porta",
        "badge": "PH",
        "company": "Porta Hnos. S.A.",
        "role": "Pasante de IT",
        "from_to": "Abr. 2024 - Feb. 2025",
        "mode": "Jornada parcial / Presencial",
        "location": "Argentina",
        "summary": "Soporte tecnico, Active Directory y sistemas corporativos en entornos productivos.",
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
    {
        "id": "datos-orange",
        "badge": "OR",
        "company": "Orange",
        "role": "Analista de datos",
        "from_to": "Mar. 2021 - May. 2022",
        "mode": "Jornada parcial / Remoto",
        "location": "Cordoba y alrededores, Argentina",
        "summary": "Gestion, normalizacion y control de calidad de datos tecnicos de infraestructura.",
        "period": "Marzo 2021 - Mayo 2022 / Jornada parcial / Remoto",
        "description": (
            "Trabaje con informacion de infraestructura electrica y telefonica, "
            "actualizando datos tecnicos, localizaciones y estructuras heterogeneas "
            "para mantener trazabilidad y calidad de informacion."
        ),
        "items": [
            "Gestion y actualizacion de archivos Excel con informacion de infraestructura electrica y telefonica.",
            "Actualizacion de localizaciones ante cambios de postes, cableado o puntos de control.",
            "Carga, normalizacion y validacion de datos tecnicos como tipo de poste, color, estado e imagenes asociadas.",
            "Control de calidad de datos y seguimiento de modificaciones para mantener trazabilidad.",
            "Trabajo con planillas avanzadas y estructuras de datos heterogeneas.",
        ],
    },
]

COMPANIES = [
    {
        "slug": "porta-hnos",
        "name": "Porta Hnos. S.A.",
        "dates": "Abr. 2024 - Actualidad",
        "summary": (
            "Crecimiento dentro del area de sistemas: soporte IT, analisis funcional "
            "del ERP corporativo y desarrollo backend con Python, Django, Azure, "
            "Grafana y Azure DevOps."
        ),
    },
    {
        "slug": "orange",
        "name": "Orange",
        "dates": "Mar. 2021 - May. 2022",
        "summary": (
            "Analisis, normalizacion y control de calidad de datos tecnicos de "
            "infraestructura electrica y telefonica, trabajando con planillas "
            "avanzadas y estructuras de datos heterogeneas."
        ),
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

SYSTEMS = [
    {
        "name": "CapHum - objetivos anuales",
        "problem": "La gestion y carga de objetivos anuales dependia de herramientas externas y procesos poco centralizados.",
        "solution": "Sistema propio para cargar, consultar y monitorear objetivos anuales, reduciendo dependencia de terceros.",
        "role": "Desarrollo backend, modelado de datos, mantenimiento de servicios y soporte a usuarios internos.",
        "tags": ["Python", "Django", "MySQL", "Azure DevOps"],
    },
    {
        "name": "HyS - gestion automatizada",
        "problem": "Procesos de higiene y seguridad se gestionaban con planillas Excel, dificultando trazabilidad y seguimiento.",
        "solution": "Digitalizacion y automatizacion de registros, consultas y flujos internos para reemplazar planillas manuales.",
        "role": "Desarrollo backend, automatizacion de procesos, soporte funcional y mejora continua.",
        "tags": ["Python", "Django", "MySQL", "Automatizacion"],
    },
    {
        "name": "Consuman",
        "problem": "Necesidad de integrar procesos internos con servicios cloud y ejecuciones desacopladas.",
        "solution": "Servicios apoyados en Azure Functions para automatizar tareas e integraciones de backend.",
        "role": "Integracion backend, despliegue cloud, mantenimiento y seguimiento operativo.",
        "tags": ["Azure Functions", "Python", "Cloud", "Integraciones"],
    },
    {
        "name": "Sistema para producción de Vinagre",
        "problem": "Procesos productivos con necesidad de seguimiento y gestion interna mas ordenada.",
        "solution": "Sistema backend para centralizar datos operativos y facilitar consultas de usuarios internos, implementación de tableros grafana para monitoreo de producción.",
        "role": "Desarrollo y mantenimiento backend, consultas de datos y soporte funcional.",
        "tags": ["Python", "Django", "MySQL", "Produccion"],
    },
    {
        "name": "sistema de gestion para Pañol",
        "problem": "Sistemas para terceros con procesos apoyados en planillas y controles manuales.",
        "solution": "Digitalizacion de flujos operativos, reduciendo uso de Excel y centralizando informacion en servicios backend.",
        "role": "Desarrollo backend, integraciones, soporte tecnico y mejora de procesos existentes.",
        "tags": ["Python", "Django", "APIs", "Terceros"],
    },
    {
        "name": "Sistema de gestion para vehiculos de empresa",
        "problem": "Seguimiento operativo distribuido en archivos Excel y registros poco integrados.",
        "solution": "Automatizacion de consultas y gestion interna para eliminar planillas dispersas y mejorar trazabilidad.",
        "role": "Analisis funcional, desarrollo backend y acompanamiento a usuarios en la adopcion del sistema.",
        "tags": ["Django", "SQL", "Automatizacion", "Operaciones"],
    },
    {
        "name": "WMS e integraciones logisticas",
        "problem": "Procesos logisticos con multiples reglas, datos maestros e integraciones operativas.",
        "solution": "Servicios backend para organizar reglas, maestros, servicios externos y operaciones del WMS.",
        "role": "Analisis tecnico, soporte funcional, consultas de datos y desarrollo de endpoints internos.",
        "tags": ["Django REST Framework", "SQL", "ERP", "WMS"],
    },
    {
        "name": "Monitoreo IoT con WebSockets",
        "problem": "Necesidad de monitorear y controlar hardware distribuido en tiempo real.",
        "solution": "Servidor WebSocket para comunicacion bidireccional con dispositivos Raspberry Pi y procesos industriales.",
        "role": "Implementacion backend, manejo de eventos, integracion con hardware y observabilidad.",
        "tags": ["Python", "Django", "WebSockets", "Raspberry Pi"],
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
        "companies": COMPANIES,
    }
    return render(request, "portfolio/experience.html", context)


def experience_detail(request, slug):
    company = next((item for item in COMPANIES if item["slug"] == slug), None)
    if company is None:
        raise Http404("Empresa no encontrada")

    company_experiences = [
        experience
        for experience in EXPERIENCES
        if experience["company"] == company["name"]
    ]
    context = base_context("experience") | {
        "company": company,
        "experiences": company_experiences,
    }
    return render(request, "portfolio/experience_detail.html", context)


def projects(request):
    context = base_context("projects") | {
        "systems": SYSTEMS,
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
