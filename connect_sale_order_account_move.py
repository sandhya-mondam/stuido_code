#account.move

#do automation on record saving 

#update code

sale_order_id = None
sale_order_rec = None
for rec in record.lines:
 sale_order_id= rec.sale_line_ids[0].order_id # sale order id 
 break

sale_order_rec = record.env['sale.order'].browse(sale_order_id)
# sale order record set 

if sale_order_rec is not None:
 record['x_studio_sale_order_id'] = sale_order_rec.id 

To update Sale order Reference number to connect account.move and sale.order '
