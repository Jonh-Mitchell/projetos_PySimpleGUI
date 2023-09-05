import PySimpleGUI as sg
import sqlite3 as bbb

# Establish a connection to the database
conn = bbb.connect("clientes.db")
c = conn.cursor()

# Create the layout for the main menu
layout = [
    [sg.Menu([
        ['Cadastro', ['Cadastro Clientes', 'Cadastrar Produtos',
                      'Cadastro Fornecedores', 'Cadastro Transportadora']],
        ['Consulta', ['Consultar Clientes', 'Consultar Produto',
                      'Consultar Fornecedores', 'Consultar Transportadora']],
        ['Relatórios', ['Relatórios de Clientes', 'Relatórios de Produtos',
                        'Relatórios de Fornecedores', 'Relatórios de Transportadoras']]
    ], tearoff=False)]
]

# Create the main window
window_cliente = sg.Window("Sistema de cadastro de clientes 1.0", layout, size=(600, 400))

# Event loop for the main window
while True:
    event, values = window_cliente.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Cadastro Clientes":
        cadastro_layout_clientes = [
            [sg.Text("Nome")],
            [sg.InputText(key="Nome")],
            [sg.Text("CPF")],
            [sg.InputText(key="CPF")],
            [sg.Text("Endereço")],
            [sg.InputText(key="Endereço")],
            [sg.Text("Telefone")],
            [sg.InputText(key="Telefone")],
            [sg.Text("Cidade")],
            [sg.InputText(key="Cidade")],
            [sg.Text("Estado")],
            [sg.InputText(key="Estado")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
            # ... (Client registration window setup)
        ]

        # Create the client registration window
        cadastro_clientes = sg.Window("Cadastro de Clientes", cadastro_layout_clientes, size=(400, 400))

        # Event loop for the client registration window
        while True:
            event, values = cadastro_clientes.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_clientes.close()
                break

            # ... (Client registration logic)
            c.execute("INSERT INTO clientes (Nome, CPF, Endereço, Telefone, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)",
                    (values["Nome"], values["CPF"], values["Endereço"], values["Telefone"], values["Cidade"], values["Estado"]))
            conn.commit()
        
            cadastro_clientes["Nome"].update("")
            cadastro_clientes["CPF"].update("")
            cadastro_clientes["Endereço"].update("")
            cadastro_clientes["Telefone"].update("")
            cadastro_clientes["Cidade"].update("")
            cadastro_clientes["Estado"].update("")
            sg.popup("Cadastro efetuado!")






    #Bloco de código de cadastro 

    elif event == "Cadastrar Produtos":
        cadastro_produto_layout = [
            [sg.Text("Produto")],
            [sg.InputText(key="produto")],
            [sg.Text("Valor")],
            [sg.InputText(key="valor")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
            # ... (Client registration window setup)
        ]

        # Create the client registration window
        cadastro_produto = sg.Window("Cadastro de Clientes", cadastro_produto_layout, size=(400, 400))

        # Event loop for the client registration window
        while True:
            event, values = cadastro_produto.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_produto.close()
                break

            # ... (Client registration logic)
            c.execute("INSERT INTO vendas (produto, valor) VALUES (?, ?)",
                    (values["produto"], values["valor"]))
            conn.commit()
        
            cadastro_produto["produto"].update("")
            cadastro_produto["valor"].update("")
            
            sg.popup("Cadastro efetuado!")
        


    elif event == "Cadastro Fornecedores":
        fornecedor_layout = [            
            # ... (Supplier registration window setup)
                [sg.Text("ID")],
                [sg.InputText(key="Id_fornecedor")],
                [sg.Text("Nome")],
                [sg.InputText(key="Nome_fornecedor")],
                [sg.Text("Endereço")],
                [sg.InputText(key="Endereço")],
                [sg.Text("CEP")],
                [sg.InputText(key="CEP")],
                [sg.Text("Cidade")],
                [sg.InputText(key="Cidade")],
                [sg.Text("Estado")],
                [sg.InputText(key="Estado")],
                [sg.Text("País")],
                [sg.InputText(key="País")],
                [sg.Button("Cadastro"), sg.Button("Cancelar")]
 
        ]

        # Create the supplier registration window
        cadastro_fornecedor = sg.Window("Cadastro de Fornecedores", fornecedor_layout, size=(400, 400))

        # Event loop for the supplier registration window
        while True:
            event, values = cadastro_fornecedor.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_fornecedor.close()
                break

            # ... (Supplier registration logic)
            c.execute("INSERT INTO fornecedores (Id_fornecedor, Nome_fornecedor, Endereço, CEP, Cidade, Estado, País) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (values["Id_fornecedor"], values["Nome_fornecedor"], values["Endereço"], values["CEP"], values["Cidade"], values["Estado"], values["País"] ))
            conn.commit()
    
            cadastro_fornecedor["Id_fornecedor"].update("")
            cadastro_fornecedor["Nome_fornecedor"].update("")
            cadastro_fornecedor["Endereço"].update("")
            cadastro_fornecedor["CEP"].update("")
            cadastro_fornecedor["Cidade"].update("")
            cadastro_fornecedor["Estado"].update("")
            cadastro_fornecedor["País"].update("") 
            sg.popup("Cadastro efetuado!")


    elif event == "Cadastro Transportadora":
        transportadora_layout = [            
            # ... (Supplier registration window setup)
                [sg.Text("ID")],
                [sg.InputText(key="Id_transportadora")],
                [sg.Text("Nome")],
                [sg.InputText(key="Nome_transportadora")],
                [sg.Text("Telefone")],
                [sg.InputText(key="Telefone")],
                [sg.Button("Cadastro"), sg.Button("Cancelar")]
 
        ]

        # Criar a janela de cadastro do fornecedor
        cadastro_transportadora = sg.Window("Cadastro de Transportadora", transportadora_layout, size=(400, 400))

        # Event loop para registrar os fornecedores no banco
        while True:
            event, values = cadastro_transportadora.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_transportadora.close()
                break

            # ... (Supplier registration logic)
            c.execute("INSERT INTO transportadora (Id_Transportadora, Nome_transportadora, Telefone) VALUES (?, ?, ?)",
                        (values["Id_transportadora"], values["Nome_transportadora"], values["Telefone"]))
            conn.commit()
    
            cadastro_transportadora["Id_transportadora"].update("")
            cadastro_transportadora["Nome_transportadora"].update("")
            cadastro_transportadora["Telefone"].update("")
            sg.popup("Cadastro efetuado!")




















    #Bloco de código de Consulta

    elif event == 'Consultar Clientes':
      
     #Atualiza o registro alterado      
        def edit_client(new_client, new_value, old_client):
           c.execute("UPDATE clientes SET Nome=?, CPF=?, Endereço=? WHERE Nome=?", (new_client, new_value, old_client))
           conn.commit()     

   #Deleta o registro escolhido
        def delete_client(client_to_delete):
            c.execute("DELETE FROM clientes WHERE Nome=?", (client_to_delete,))
            conn.commit()

        consulta_layout = [
            [sg.Text("Nome:")],
            [sg.InputText(key="Nome")],

            [sg.Button("Consultar")],
            [sg.Table(values=[], headings=["Nome", "CPF", "Endereço", "Telefone", "Cidade", "Estado"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela" )],
            [sg.Button("Editar"), sg.Button("Excluir"), sg.Button("Cancelar")]
        ]

        window_consulta_client = sg.Window("Consulta de Clientes", consulta_layout, resizable=True)

        while True:
            event, values = window_consulta_client.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                break

            if event == "Consultar":
                client_consulta = values["Nome"].upper()
                c.execute("SELECT Nome, CPF FROM clientes WHERE UPPER(Nome) = ?", (client_consulta,))
                registros = c.fetchall()

                window_consulta_client["tabela"].update(values=registros)

            elif event == "Editar":
                selected_row = values["tabela"]
                if selected_row:
                    selected_row_index = selected_row[0]
                    row_data = registros[selected_row_index]
                    # Edita nome e valor de um produto
                    edited_client = sg.popup_get_text("Editar Nome, CPF:", default_text=row_data[0] + "," + row_data[1] + "," + row_data[2])
                    if edited_client is not None:
                        edited_client, edited_cpf, edited_end = edited_client.split(',')
                        old_client = row_data[0]
                        
                        if edited_client != old_client:
                            edit_client(edited_client, row_data[1], old_client)
                        if edited_cpf != row_data[1]:
                            edit_client(edited_client, edited_cpf, edited_client)
                        if edited_end!= row_data[2]:
                            edit_record(edited_client, edited_end, edited_client)  
                        if edited_tel != row_data[3]:
                            edit_record(edited_client, edited_end, edited_client)
                        if edited_city != row_data[4]:
                            edit_record(edited_client, edited_cit, edited_client)
                        if edited_est != row_data[5]:
                            edit_record(edited_client, edited_est, edited_client)
                         
                        registros[selected_row_index] = (edited_client, edited_cpf, edited_end)
                        window_consulta_client["tabela"].update(values=registros)
                    
            elif event == "Excluir":
                selected_row = values["tabela"]
                if selected_row:
                    selected_row_index = selected_row[0]
                    row_data = registros[selected_row_index]
                    if sg.popup_yes_no("Tem certeza que deseja excluir este registro?", title="Confirmação") == "Yes":
                        product_to_delete = row_data[0]
                        delete_client(product_to_delete)
                        registros.pop(selected_row_index)
                        window_consulta_client["tabela"].update(values=registros)
                        #consulta_window_client["tabela"].update(values=registros)

        window_consulta_client.close()


    elif event == 'Consultar Produto':
      
     #Atualiza o registro alterado      
        def edit_record(new_product, new_value, old_product):
           c.execute("UPDATE vendas SET produto=?, valor=? WHERE produto=?", (new_product, new_value, old_product))
           conn.commit()     

   #Deleta o registro escolhido
        def delete_record(product_to_delete):
            c.execute("DELETE FROM vendas WHERE produto=?", (product_to_delete,))
            conn.commit()

        layout_consulta_prod = [
            [sg.Text("Produto:")],
            [sg.InputText(key="produto")],
            [sg.Button("Consultar")],
            [sg.Table(values=[], headings=["Produto", "Valor"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")],
            [sg.Button("Editar"), sg.Button("Excluir"), sg.Button("Cancelar")]
        ]

        window_consulta_prod = sg.Window("Consulta", layout_consulta_prod, resizable=True)

        while True:
            event, values = window_consulta_prod.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                break

            if event == "Consultar":
                produto_busca = values["produto"].upper()
                c.execute("SELECT produto, valor FROM vendas WHERE UPPER(produto) = ?", (produto_busca,))
                registros = c.fetchall()

                window_consulta_prod["tabela"].update(values=registros)

            elif event == "Editar":
                selected_row = values["tabela"]
                if selected_row:
                    selected_row_index = selected_row[0]
                    row_data = registros[selected_row_index]
                    # Edita nome e valor de um produto
                    edited_product = sg.popup_get_text("Editar Produto e Valor:", default_text=row_data[0] + "," + row_data[1])
                    if edited_product is not None:
                        edited_product, edited_value = edited_product.split(',')
                        old_product = row_data[0]
                        
                        if edited_product != old_product:
                            edit_record(edited_product, row_data[1], old_product)
                        if edited_value != row_data[1]:
                            edit_record(edited_product, edited_value, edited_product)
                            
                        registros[selected_row_index] = (edited_product, edited_value)
                        window_consulta_prod["tabela"].update(values=registros)
                    

            elif event == "Excluir":
                selected_row = values["tabela"]
                if selected_row:
                    selected_row_index = selected_row[0]
                    row_data = registros[selected_row_index]
                    if sg.popup_yes_no("Tem certeza que deseja excluir este registro?", title="Confirmação") == "Yes":
                        product_to_delete = row_data[0]
                        delete_record(product_to_delete)
                        registros.pop(selected_row_index)
                        window_consulta_prod["tabela"].update(values=registros)

        window_consulta_prod.close()
















    #Bloco de codigo de relatório

    elif event == "Relatórios de Produtos":
            relatorio_layout = [            
                # ... (Supplier registration window setup)
                    [sg.Text("Produto")],
                    [sg.InputText(key="produto")],
                    [sg.Button("Gerar relatório"), sg.Button("Cancelar")]
    
            ]


            # Criar a janela de cadastro do fornecedor
            relatorio_window = sg.Window("Relatório", relatorio_layout, resizable=True)

            # Event loop para registrar os fornecedores no banco
            while True:
                event, values = relatorio_window.read()

                if event == sg.WINDOW_CLOSED or event == "Cancelar":
                    relatorio_window.close()
                    break

                # ... (Supplier registration logic)
                produto_busca = values["produto"].upper()
                c.execute("SELECT * FROM vendas WHERE UPPER(produto) = ?", (produto_busca,))
                registro = c.fetchone()

                if registro:

                    with open("C:/Users/alunosenac/Área de trabalho/project_Desktop_Python-main/relatorio-prod", "w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório</h1><table border='1'><tr><th>Produtos</th><th>Valor</th></tr>")
                        f.write(f"<tr><th>{registro[0]}</th><th>{registro[1]}</th></tr>")
                        f.write("</body></html>")
                
                    sg.popup("Relatório gerado com sucesso!", title="Relatório")
                
                else:
                    sg.popup("Produto não encontrado no banco de dados!", title="Relatório")

                relatorio_window["produto"].update("")

    elif event == "Relatórios de Clientes":
            relatorio_client_layout = [            
                # ... (Supplier registration window setup)
                    [sg.Text("Nome")],
                    [sg.InputText(key="Nome")],
                    [sg.Button("Gerar relatório"), sg.Button("Cancelar")]
    
            ]


            # Criar a janela de cadastro do fornecedor
            relatorio_client_window = sg.Window("Relatório", relatorio_client_layout, resizable=True)

            # Event loop para registrar os fornecedores no banco
            while True:
                event, values = relatorio_client_window.read()

                if event == sg.WINDOW_CLOSED or event == "Cancelar":
                    relatorio_client_window.close()
                    break

                # ... (Supplier registration logic)
                client_busca = values["Nome"].upper()
                c.execute("SELECT * FROM clientes WHERE UPPER(Nome) = ?", (client_busca,))
                registro_client = c.fetchone()

                if registro_client:

                    with open("C:/Users/alunosenac/Área de trabalho/project_Desktop_Python-main/relatorio-cli", "w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório</h1><table border='1'><tr><th>Nome</th><th>CPF</th><th>Endereço</th><th>Telefone</th><th>Cidade</th><th>Estado</th></tr>")
                        f.write(f"<tr><th>{registro_client[0]}</th><th>{registro_client[1]}</th><th>{registro_client[2]}</th><th>{registro_client[3]}</th><th>{registro_client[4]}</th><th>{registro_client[5]}</th></tr>")
                        f.write("</body></html>")
                
                    sg.popup("Relatório gerado com sucesso!", title="Relatório")
                
                else:
                    sg.popup("Produto não encontrado no banco de dados!", title="Relatório")

                relatorio_client_window["Nome"].update("")   



    elif event == "Relatórios de Fornecedores":
            report_supplier_layout = [            
                # ... (Supplier registration window setup)
                    [sg.Text("Nome")],
                    [sg.InputText(key="Nome_fornecedor")],
                    [sg.Button("Gerar relatório"), sg.Button("Cancelar")]
    
            ]


            # Criar a janela de cadastro do fornecedor
            repport_supplier_window = sg.Window("Relatório", report_supplier_layout, resizable=True)

            # Event loop para registrar os fornecedores no banco
            while True:
                event, values = repport_supplier_window.read()

                if event == sg.WINDOW_CLOSED or event == "Cancelar":
                    repport_supplier_window.close()
                    break

                # ... (Supplier registration logic)
                supplier_search = values["Nome_fornecedor"].upper()
                c.execute("SELECT * FROM fornecedores WHERE UPPER(Nome_fornecedor) = ?", (supplier_search,))
                #record_supplier = c.fetchone()
                record_supplier = c.fetchone()

                if record_supplier:

                    with open("C:/Users/alunosenac/Área de trabalho/project_Desktop_Python-main/relatorio-forn", "w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório</h1><table border='1'><tr><th>ID Supplier</th><th>Name</th><th>Address</th><th>Postal Code</th><th>C</th><th>City</th><th>State</th><th>Country</th></tr>")
                            
                       # for row in registro_f:
                        f.write("<tr><td>{row[0]}</td><td>{row[1]}</td></tr>")
                       #f.write("</table></body></html>")
                        f.write(f"<tr><th>{record_supplier[0]}</th><th>{record_supplier[1]}</th><th>{record_supplier[2]}</th><th>{record_supplier[3]}</th><th>{record_supplier[4]}</th><th>{record_supplier[5]}</th></tr>")
                        #f.write("</body></html>")
                
                    sg.popup("Relatório gerado com sucesso!", title="Relatório")
                
                else:
                    sg.popup("Produto não encontrado no banco de dados!", title="Relatório")

                repport_supplier_window["Nome_fornecedor"].update("") 
    


# Close all windows and the database connection
window_cliente.close()
conn.close()