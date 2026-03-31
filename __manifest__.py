{
    'name': 'Reporte de Factura Personalizado (ARCA Style)',
    'version': '17.0',
    'category': 'Accounting/Localizations',
    'summary': 'Reporte QWeb para facturas con diseño específico de ARCA.',
    'depends': ['account', 'l10n_ar'], # Importante para campos como CAE y CUIT
    'data': [
        'reports/report_invoice_definition.xml',
        'reports/report_invoice_template.xml',
    ],
    'installable': True,
    'application': False,
}