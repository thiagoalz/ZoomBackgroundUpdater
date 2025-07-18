# ZoomBackgroundUpdater

Script em Python para adicionar automaticamente uma contagem regressiva em uma imagem de fundo do Zoom ou Microsoft Teams.

## Requisitos

- Python 3
- Biblioteca [Pillow](https://pillow.readthedocs.io/) (`pip install pillow`)

## Configuração

1. Clone este repositório ou copie os arquivos `FundoZeCopa.py`, `FundoZeCopa.png` e `GaroaHackerClubeBold.otf` para uma pasta de sua preferência.
2. Edite o arquivo `FundoZeCopa.py` e ajuste as variáveis de configuração:
   - `original_image_path`: caminho para a imagem de fundo base (padrão `FundoZeCopa.png`).
   - `arquivo_fundo_zoom`: caminho para o arquivo de plano de fundo utilizado pelo Zoom.
   - `arquivo_fundo_teams`: caminho para o arquivo de plano de fundo utilizado pelo Microsoft Teams (opcional).
   - `title_text`: texto exibido na imagem. Use `{}` para inserir o número de dias restante.
   - `countdown_date_text`: data final da contagem regressiva (formato `AAAA-MM-DD`).
   - Opções de fonte, cor, tamanho e posição do texto podem ser ajustadas nas variáveis `font_path`, `font_size`, `text_color`, `text_stroke_color`, `text_stroke_width`, `width_text_pos` e `height_text_pos`.

## Uso

Execute o script com:

```bash
python3 FundoZeCopa.py
```

O script gerará um arquivo `FundoZeCopaResult.jpg` com a contagem regressiva. Se os caminhos para `arquivo_fundo_zoom` ou `arquivo_fundo_teams` estiverem configurados, esse arquivo será copiado automaticamente para substituir o plano de fundo utilizado pela aplicação.

Para atualizar diariamente o plano de fundo, configure seu sistema operacional para executar o script em intervalos regulares (por exemplo, utilizando o agendador de tarefas do Windows ou `cron` no macOS/Linux).

## Personalização

- Altere o texto do contador em `title_text` para outras mensagens.
- Modifique `countdown_date_text` para fazer contagem regressiva até outra data.
- Ajuste o tamanho, fonte e cores do texto conforme desejar.
- Você pode utilizar outra imagem de fundo mudando `original_image_path` para o caminho da imagem desejada.

## Exemplo de diretórios do Zoom e Teams

- **Windows**
  - Zoom: `C:\Users\Usuario\AppData\Roaming\Zoom\data\VirtualBkgnd_Custom\{FFCB4691-A4F1-4031-AD05-C62BA8B7510D}`
  - Teams: `C:\Users\Usuario\AppData\Roaming\Microsoft\Teams\Backgrounds\Uploads\FundoZeCopa.png`
- **macOS**
  - Zoom: `/Users/Usuario/Library/Application Support/zoom.us/data/VirtualBkgnd_Custom/63327A14-224B-49B1-8E66-30AF4686089A`

A localização exata pode variar. Crie um novo plano de fundo e procure pelo arquivo mais recente na pasta correspondente.

## Licença

Este projeto é distribuído sem licença específica. Utilize por sua conta e risco.

