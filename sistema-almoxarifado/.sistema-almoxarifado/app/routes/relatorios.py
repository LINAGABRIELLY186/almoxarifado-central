import os
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import extract
from typing import Optional

from app.database.connection import get_db
from app.database.models import Movimentacao, Setor, Produto

router = APIRouter()

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DIRETORIO_TEMPLATES = os.path.join(DIRETORIO_ATUAL, "..", "templates")
templates = Jinja2Templates(directory=DIRETORIO_TEMPLATES)

@router.get("/html/setores", response_class=HTMLResponse)
def relatorio_setores(
    request: Request, 
    setor_id: Optional[int] = None, 
    produto_id: Optional[int] = None, 
    mes: Optional[str] = None, 
    db: Session = Depends(get_db)
):
    """Gera o extrato de consumo permitindo filtrar por Setor, Produto e Mês."""
    query = db.query(Movimentacao)
    
    # Filtro por Setor
    if setor_id:
        query = query.filter(Movimentacao.setor_id == setor_id)
        
    # Filtro por Produto
    if produto_id:
        query = query.filter(Movimentacao.produto_id == produto_id)
        
    # Filtro por Mês (formato YYYY-MM)
    if mes:
        try:
            ano, mes_num = mes.split("-")
            query = query.filter(
                extract('year', Movimentacao.data_movimentacao) == int(ano),
                extract('month', Movimentacao.data_movimentacao) == int(mes_num)
            )
        except ValueError:
            pass
        
    movimentacoes = query.order_by(Movimentacao.data_movimentacao.desc()).all()
    setores = db.query(Setor).order_by(Setor.nome).all()
    produtos = db.query(Produto).order_by(Produto.nome).all()
    
    return templates.TemplateResponse(
        request=request,
        name="relatorios/setores.html",
        context={
            "request": request,
            "movimentacoes": movimentacoes,
            "setores": setores,
            "produtos": produtos,
            "setor_selecionado": setor_id,
            "produto_selecionado": produto_id,
            "mes_selecionado": mes
        }
    )