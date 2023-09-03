CREATE DEFINER = CURRENT_USER TRIGGER `control`.`tblmovest_BEFORE_DELETE` BEFORE DELETE ON `tblmovest` FOR EACH ROW
BEGIN
	-- Verifica se existem lançamentos na tbllan referenciando o código de movimentação sendo excluído
    DECLARE references_count INT;
    
    SELECT COUNT(*) INTO references_count
    FROM tbllan
    WHERE CODMOVEST = OLD.CODMOVEST;
    
    IF references_count > 0 THEN
        -- Remove as referências na tbllan
        UPDATE tbllan
        SET CODMOVEST = NULL
        WHERE CODMOVEST = OLD.CODMOVEST;
    END IF;
END
