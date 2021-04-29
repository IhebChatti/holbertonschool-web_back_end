-- script that creates a trigger that decreases
-- the quantity of an item after adding a new order.

DROP TRIGGER IF EXISTS `MyTrigger`;
CREATE TRIGGER `MyTrigger` 
AFTER INSERT ON `orders`
FOR EACH ROW 
BEGIN
	UPDATE items
		SET quantity = quantity - New.quantity
		WHERE name=New.item_name;
END;
