for rec in records:

    source = rec.x_studio_sector_3
    
    source_name = source.x_name if source and source.x_name else ""
   
    
    if source_name.count("/") >= 4:
        # Split the string into two parts
        parts = source_name.split("/")
        
        #BAH/BOM/DEL/DXB/BAH  --> 
        #BAH/BOM/DEL/DXB --> First Part
        #BAH --> Second Part
        str2 = "/".join(parts[:4]) 
        str3 = "/".join(parts[4:]) 
        final_source = str2 + '-' + str3
        record.x_studio_sector_3.write({'x_name': final_source})
        rec.write({'x_studio_destination1': source_name[(len(source_name)-3):len(source_name)]})
        rec.write({'x_studio_destination2': ''})
        rec.write({'x_studio_destination3': ''})
        
        product = rec.env['product.product'].search([('name', '=', 'conjunction')], limit=1)
        ticket_no_list = []
        ticket_no = 0
        counter = 0
        for line in rec.order_line:
            ticket_no_list.append(line.x_studio_ticket_number)
            # check conjuction value and then increment the number in ticket no and then create new values
            # pre ticket no = 2762827282
            # pre ticket no updated to = 2762827282-283
            # new ticket no updated to = 2762827283-282
            old_ticket_last_3_dig = int(ticket_no_list[counter])[-3:]
            updated_next_ticket_no = int(old_ticket_last_3_dig) + 1
            last_new_no = int(ticket_no_list[counter])[-3:] + 1
            ticket_no = ticket_no_list[counter] + '-' + str(last_new_no)
            line.x_studio_ticket_number = ticket_no
            new_ticket_no = updated_next_ticket_no + '-' + str(old_ticket_last_3_dig)
            
            counter += 1
            env['sale.order.line'].create({
                'order_id': rec.id,
                'product_template_id': product.id,
                'x_studio_ticket_number': new_ticket_no,
                'name': product.name 
            })
        
        
        
        # product = rec.env['product.product'].search([('name', '=', 'conjunction')], limit=1)
        # env['sale.order.line'].create({
        #     'order_id': rec.id,
        #     'product_template_id': product.id,
        #     'x_studio_ticket_number': 2762827282,
        #     'name': product.name 
        # })
    
            
    
    
    

    # elif len(source_name) == 7:
        
    #     rec.write({'x_studio_destination1': source_name[4:7]})
    #     rec.write({'x_studio_destination2': ''})
        
    #     rec.write({'x_studio_destination3': ''})
    
    # elif len(source_name) == 11:
    #     #DXB/BOM
    #     rec.write({'x_studio_destination1': source_name[4:7]})
        
        
    #     #DXB/BOM/BKK
    #     rec.write({'x_studio_destination2': source_name[8:11]})
        
    #     rec.write({'x_studio_destination3': ''})
        
    # elif len(source_name)==15:
    #     #DXB/BOM
    #     rec.write({'x_studio_destination1': source_name[4:7]})
        
    #     #DXB/BOM/BKK
    #     rec.write({'x_studio_destination2': source_name[8:11]})
        
    #     #DXB/BOM/BKK/BOM
    #     rec.write({'x_studio_destination3': source_name[12:15]})
    

    #     # rec.write({'x_studio_sector_3':final_source})
        
  This code is for conjuction tickets 
