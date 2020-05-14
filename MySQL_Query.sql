select * from orderai join vender on vender.VenderNo = orderai.VenderNo;

select VenderNo,count(*) from orderai group by VenderNo;

select * from order_spare_parts limit 100;

select VenderNO,count(*) from order_spare_parts group by VenderNo;

select * from vender;


select count(*) from orderai group by ItemCode;

select ItemCode, ItemDesc, vender.VenderNo, vender.VenderDesc  from order_spare_parts inner join vender on order_spare_parts.VenderNo = vender.VenderNo
order by VenderNo desc;

select ItemCode,ItemDesc ,count(*) from order_spare_parts where VenderNo = '004' group by ItemCode;