select ItemCode,ItemDesc ,count(*) from order_spare_parts where VenderNo = '004' group by ItemCode;