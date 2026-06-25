# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

NAVY = HexColor("#03111F")
GRAY = HexColor("#737373")
GRAY_LIGHT = HexColor("#F3F4F6")
WHITE = HexColor("#FFFFFF")

styles = getSampleStyleSheet()

style_brand = ParagraphStyle(
    "brand", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=12, textColor=NAVY, letterSpacing=1, spaceAfter=2,
)
style_eyebrow = ParagraphStyle(
    "eyebrow", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=8.5, textColor=GRAY, spaceAfter=6,
)
style_title = ParagraphStyle(
    "title", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=20, textColor=NAVY, leading=24, spaceAfter=4, alignment=TA_LEFT,
)
style_sub = ParagraphStyle(
    "sub", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10.5, textColor=GRAY, leading=14, spaceAfter=14,
)
style_item_title = ParagraphStyle(
    "item_title", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10.5, textColor=NAVY, leading=13,
)
style_item_desc = ParagraphStyle(
    "item_desc", parent=styles["Normal"], fontName="Helvetica",
    fontSize=9, textColor=GRAY, leading=12,
)
style_conclusion_title = ParagraphStyle(
    "conclusion_title", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=12, textColor=WHITE, leading=15, spaceAfter=6,
)
style_conclusion_body = ParagraphStyle(
    "conclusion_body", parent=styles["Normal"], fontName="Helvetica",
    fontSize=9.5, textColor=WHITE, leading=14,
)
style_cta = ParagraphStyle(
    "cta", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10.5, textColor=NAVY, leading=14, alignment=TA_CENTER,
)
style_footer = ParagraphStyle(
    "footer", parent=styles["Normal"], fontName="Helvetica",
    fontSize=8, textColor=GRAY, alignment=TA_CENTER,
)


def checkbox_drawing():
    size = 11
    d = Drawing(size, size)
    d.add(Rect(0, 0, size, size, strokeColor=NAVY, strokeWidth=1.2, fillColor=None))
    return d


def checklist_table(items):
    rows = []
    for title, desc in items:
        cell = [
            Paragraph(title, style_item_title),
            Paragraph(desc, style_item_desc),
        ]
        rows.append([checkbox_drawing(), cell])
    t = Table(rows, colWidths=[10 * mm, 150 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (0, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (1, 0), (1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, GRAY_LIGHT),
    ]))
    return t


def conclusion_block(title, body):
    inner = Table(
        [[Paragraph(title, style_conclusion_title)], [Paragraph(body, style_conclusion_body)]],
        colWidths=[170 * mm],
    )
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
    ]))
    return inner


def build(filename, eyebrow, title, sub, items, conclusion_title, conclusion_body, cta):
    doc = SimpleDocTemplate(
        filename, pagesize=A4,
        leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=16 * mm, bottomMargin=16 * mm,
    )
    story = []
    story.append(Paragraph("QUALIORG CONSULTORIA", style_brand))
    story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=12))
    story.append(Paragraph(eyebrow, style_eyebrow))
    story.append(Paragraph(title, style_title))
    story.append(Paragraph(sub, style_sub))
    story.append(checklist_table(items))
    story.append(Spacer(1, 10))
    story.append(conclusion_block(conclusion_title, conclusion_body))
    story.append(Spacer(1, 14))
    story.append(Paragraph(cta, style_cta))
    story.append(Spacer(1, 18))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GRAY_LIGHT, spaceAfter=8))
    story.append(Paragraph(
        "Qualiorg Consultoria &nbsp;|&nbsp; fernando@qualiorg.com.br &nbsp;|&nbsp; (11) 99862-3467 &nbsp;|&nbsp; qualiorg.com.br",
        style_footer,
    ))
    doc.build(story)


iso9001_items = [
    ("1. Liderança comprometida",
     "A alta direção participa ativamente do sistema de gestão da qualidade, definindo responsabilidades e cobrando resultados — não apenas delegando ao setor de qualidade."),
    ("2. Política da qualidade definida",
     "Existe uma política da qualidade formal, comunicada a todos os colaboradores e alinhada aos objetivos estratégicos da empresa."),
    ("3. Mapeamento de processos",
     "Os principais processos da empresa estão mapeados, com entradas, saídas, responsáveis e indicadores claramente definidos."),
    ("4. Gestão de riscos e oportunidades",
     "A empresa identifica, avalia e trata riscos e oportunidades que podem afetar a conformidade de produtos e serviços."),
    ("5. Controle de documentos",
     "Procedimentos, instruções de trabalho e registros são controlados, com versões atualizadas e acesso facilitado para quem precisa."),
    ("6. Competência e treinamento da equipe",
     "Colaboradores possuem a competência necessária para suas funções, com treinamentos registrados e eficácia avaliada."),
    ("7. Controle operacional",
     "Os processos de produção ou prestação de serviço são executados sob condições controladas, com critérios claros de aceitação."),
    ("8. Monitoramento e medição",
     "Indicadores de desempenho dos processos são acompanhados periodicamente, com metas definidas e dados confiáveis."),
    ("9. Não conformidades e ações corretivas",
     "Não conformidades são registradas, analisadas quanto à causa raiz e tratadas com ações corretivas eficazes."),
    ("10. Auditoria interna",
     "A empresa realiza auditorias internas periódicas para verificar a conformidade e eficácia do sistema de gestão."),
    ("11. Análise crítica pela direção",
     "A direção realiza reuniões periódicas para analisar o desempenho do sistema de gestão e decidir melhorias."),
]

iec_items = [
    ("1. Sistema de gestão da qualidade para reparo Ex",
     "A empresa possui um sistema de gestão da qualidade implantado especificamente para as atividades de reparo e revisão de equipamentos Ex."),
    ("2. Pessoal qualificado e certificado",
     "Os técnicos que executam reparos em área classificada possuem qualificação e certificação formal para esse tipo de trabalho."),
    ("3. Procedimentos por tipo de proteção",
     "Existem procedimentos documentados específicos para cada tipo de proteção trabalhado (Ex d, Ex e, Ex i, Ex p, entre outros)."),
    ("4. Controle de pintura e revestimento",
     "Processos de pintura e revestimento seguem rigorosamente a especificação original do fabricante do equipamento."),
    ("5. Testes e inspeções pós-reparo",
     "Todo equipamento reparado passa por testes e inspeções que comprovam a manutenção da integridade da proteção contra explosão."),
    ("6. Rastreabilidade de peças e materiais",
     "Peças e materiais utilizados no reparo são rastreáveis, com registro de origem e especificação técnica."),
    ("7. Marcação e identificação do equipamento",
     "O equipamento reparado é identificado conforme exigido pela norma, indicando que passou por reparo certificado."),
    ("8. Registros de reparo arquivados",
     "Todos os reparos realizados geram registros completos, arquivados e disponíveis para consulta e auditoria."),
    ("9. Auditoria periódica do processo",
     "O processo de reparo Ex é auditado periodicamente para garantir conformidade contínua com a IEC 60079-19."),
]

build(
    "checklist-iso9001.pdf",
    "AUTODIAGNÓSTICO GRATUITO",
    "Está sua empresa pronta para a ISO 9001?",
    "Responda este checklist rápido e descubra o quão preparada sua empresa está para implementar ou manter "
    "a certificação ABNT NBR ISO 9001. Marque os itens que sua empresa já atende.",
    iso9001_items,
    "O que o seu resultado significa?",
    "Se você marcou menos de 60% dos itens acima, é um forte sinal de que sua empresa ainda não está "
    "estruturada para obter ou manter a certificação ISO 9001 com segurança. Isso não é um problema raro — "
    "a maioria das empresas em fase de implantação se encontra exatamente nesse ponto. O importante é contar "
    "com apoio especializado para organizar essas lacunas antes da auditoria de certificação.",
    "Quer ajuda para implementar? Solicite um orçamento gratuito: qualiorg.com.br/orcamento.html",
)

build(
    "checklist-iec60079-19.pdf",
    "AUTODIAGNÓSTICO GRATUITO",
    "Sua empresa está em conformidade com a IEC 60079-19?",
    "Este checklist ajuda empresas que reparam e revisam equipamentos elétricos para áreas classificadas a "
    "identificar lacunas de conformidade com a ABNT NBR IEC 60079-19. Marque os itens que sua empresa já atende.",
    iec_items,
    "O que o seu resultado significa?",
    "Se você marcou menos de 60% dos itens acima, sua empresa pode estar exposta a riscos de segurança e "
    "não conformidade em auditorias — um problema crítico em operações com áreas classificadas. A boa notícia "
    "é que essas lacunas podem ser corrigidas com um plano estruturado de adequação à norma.",
    "Quer ajuda para implementar? Solicite um orçamento gratuito: qualiorg.com.br/orcamento.html",
)

print("OK: PDFs gerados.")
