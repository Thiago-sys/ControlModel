CREATE DEFINER=`root`@`localhost` TRIGGER `tbllan_BEFORE_INSERT` BEFORE INSERT ON `tbllan` FOR EACH ROW BEGIN
	DECLARE item_quantity INT;
    DECLARE existing_quantity INT;
    DECLARE new_movest_code INT;

    -- Obtém a quantidade do item no estoque
    SELECT QTD INTO item_quantity
    FROM tblest
    WHERE CODITE = NEW.CODITE;

    -- Verifica o tipo de movimentação
    IF NEW.NATLAN = 'V' THEN
        -- Caso seja uma venda, verifica se a quantidade vendida está disponível
        IF item_quantity >= NEW.QTDITE THEN
            -- Insere na tabela tblmovest
            INSERT INTO tblmovest (DTAMOV, CODITE, QTD, NATMOV, CODCLI, COMMOV)
            VALUES (NEW.DTALAN, NEW.CODITE, NEW.QTDITE, NEW.NATLAN, NEW.CODCLI, NEW.COMLAN);
            
            -- Obtém o novo código de movimentação inserido
            SET new_movest_code = LAST_INSERT_ID();
            -- Atualiza o campo CODMOVEST na tabela tbllan
            SET NEW.CODMOVEST = new_movest_code;
            
            -- Atualiza a quantidade no estoque
            UPDATE tblest
            SET QTD = QTD - NEW.QTDITE
            WHERE CODITE = NEW.CODITE;
        ELSE
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Quantidade insuficiente no estoque para a venda';
        END IF;
    ELSEIF NEW.NATLAN = 'C' THEN
        -- Caso seja uma compra
        -- Verifica se o item já existe no estoque
        SELECT QTD INTO existing_quantity
        FROM tblest
        WHERE CODITE = NEW.CODITE;
        
        IF existing_quantity IS NOT NULL THEN
            -- Atualiza a quantidade no estoque
            UPDATE tblest
            SET QTD = QTD + NEW.QTDITE
            WHERE CODITE = NEW.CODITE;
        ELSE
            -- Insere um novo registro no estoque
            INSERT INTO tblest (CODITE, QTD)
            VALUES (NEW.CODITE, NEW.QTDITE);
        END IF;

        -- Insere na tabela tblmovest
        INSERT INTO tblmovest (DTAMOV, CODITE, QTD, NATMOV, CODFOR, COMMOV)
        VALUES (NEW.DTALAN, NEW.CODITE, NEW.QTDITE, NEW.NATLAN, NEW.CODFOR, NEW.COMLAN);
        
        -- Obtém o novo código de movimentação inserido
		SET new_movest_code = LAST_INSERT_ID();
		-- Atualiza o campo CODMOVEST na tabela tbllan
		SET NEW.CODMOVEST = new_movest_code;
    END IF;
END