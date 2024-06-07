# Projeto com TDD

Esse projeto aplica os conceitos de TDD. Faz parte do curso de TDD com FastAPI ministrador pela Nayanna [https://www.linkedin.com/in/nayannanara/] pela DIO.

## Desafio Final

* Create
  * Mapear uma exceção, caso dê algum erro de inserção e capturar na controller
* Update
  * Modifique o método de patch para retornar uma exeção de Nof Found, quando o dado não for encontrado
  * a exceção deve ser tratada na controller, para ser retornada uma mensagem amigável para o usuário
  * ao alterar um dado, a data de update_at deve corresponder a data atual, permitir modificar update_at também
* Filtros
  * cadastre produtos com preços diferentes
  * aplique um filtro de preços, assim (prive > 5000 and price < 8000)
