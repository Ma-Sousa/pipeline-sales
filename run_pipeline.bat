@echo off
setlocal

echo ================================
echo Rodando pipeline de limpeza...
echo ================================

REM Garante que o comando rode a partir da raiz do projeto
cd /d "%~dp0"

python src\clean_data.py

echo.
echo ================================
echo Finalizado!
echo Verifique o arquivo:
echo data\processed\sales_clean.csv
echo ================================
pause
