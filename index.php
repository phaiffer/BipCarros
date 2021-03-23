<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Agenda de contatos</title>
    </head>
    <body>
        <form action="?act=save" method="POST" name="form1" >
          <h1>Agenda de contatos</h1>
          <hr>
          <input type="hidden" name="id" />
          Tag:
          <input type="text" name="tags" />
         <input type="submit" value="salvar" />
         <input type="reset" value="Novo" />
         <hr>
       </form>
    <table border="1" width="20%">
        <tr>
            <th>Tag</th>
        </tr>
    </table>
    </body>
</html>