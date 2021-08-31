from datetime import date, datetime


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')
# recebe um valor no formato date e devolve no no formato str


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')
# recebe um valor no formato str e devolve no formato date


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'
