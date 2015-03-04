--
-- Add ir model data before update pyme to not create new records
--

--
-- Mailboxs
--

insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    1,
    'pyme',
    '[["name", "Enviado"]]',
    'electronic_mail_mailbox_send',
    'electronic.mail.mailbox',
    '[["name", "Enviado"]]'
    );
insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    2,
    'pyme',
    '[["name", "Borrador"]]',
    'electronic_mail_mailbox_draft',
    'electronic.mail.mailbox',
    '[["name", "Borrador"]]'
    );
insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    3,
    'pyme',
    '[["name", "Error"]]',
    'electronic_mail_mailbox_error',
    'electronic.mail.mailbox',
    '[["name", "Error"]]'
    );
insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    4,
    'pyme',
    '[["name", "Salida"]]',
    'electronic_mail_mailbox_outbox',
    'electronic.mail.mailbox',
    '[["name", "Salida"]]'
    );

--
-- Party
--

insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    (
    select distinct on (model)
        id
    from
        electronic_mail_template
    where
        model in (
        select
            id
        from
            ir_model
        where
            model = 'party.party'
        )
        ),
    'pyme',
    '[["engine", "genshi"], ["from_", "user@demo_server.com"], ["html", ""], ["language", "${record.lang and record.lang.code or ''es_ES''}"], ["model", 85], ["name", "Party eMail"], ["plain", ""], ["signature", true], ["smtp_server", 8], ["subject", "${record.name}"], ["to", "${'',''.join([x.email for x in record.addresses if x.email]) or record.get_mechanism(''email'') or ''''}"]]',
    'party_email_template',
    'electronic.mail.template',
    '[["engine", "genshi"], ["from_", "user@demo_server.com"], ["html", ""], ["language", "${record.lang and record.lang.code or ''es_ES''}"], ["model", 85], ["name", "Party eMail"], ["plain", ""], ["signature", true], ["smtp_server", 8], ["subject", "${record.name}"], ["to", "${'',''.join([x.email for x in record.addresses if x.email]) or record.get_mechanism(''email'') or ''''}"]]'
    );

--
-- Address
--

insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    (
    select distinct on (model)
        id
    from
        electronic_mail_template
    where
        model in (
        select
            id
        from
            ir_model
        where
            model = 'party.address'
        )
        ),
    'pyme',
    '[["engine", "genshi"], ["from_", "user@demo_server.com"], ["html", ""], ["language", "${record.party.lang and record.party.lang.code or ''es_ES''}"], ["model", 89], ["name", "Contact eMail"], ["plain", ""], ["signature", true], ["smtp_server", 8], ["subject", "Subject ${record.name}"], ["to", "${record.email or record.party.get_mechanism(''email'') or ''''}"]]',
    'contact_email_template',
    'electronic.mail.template',
    '[["engine", "genshi"], ["from_", "user@demo_server.com"], ["html", ""], ["language", "${record.lang and record.lang.code or ''es_ES''}"], ["model", 85], ["name", "Party eMail"], ["plain", ""], ["signature", true], ["smtp_server", 8], ["subject", "${record.name}"], ["to", "${'',''.join([x.email for x in record.addresses if x.email]) or record.get_mechanism(''email'') or ''''}"]]'
    );

--
-- Account Invoice
--

insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    (
    select distinct on (model)
        id
    from
        electronic_mail_template
    where
        model in (
        select
            id
        from
            ir_model
        where
            model = 'account.invoice'
        )
        ),
    'pyme',
    '[["engine", "genshi"], ["from_", "user@demo_server.com"], ["html", ""], ["language", "${record.party.lang and record.party.lang.code or ''es_ES''}"], ["model", 170], ["name", "Invoice eMail"], ["plain", ""], ["signature", true], ["smtp_server", 8], ["subject", "Factura ${record.number or record.party.name}"], ["to", "${record.party.get_mechanism(''email'') or ''''}"]]',
    'invoice_email_template',
    'electronic.mail.template',
    '[["engine", "genshi"], ["from_", "user@demo_server.com"], ["html", ""], ["language", "${record.party.lang and record.party.lang.code or ''es_ES''}"], ["model", 170], ["name", "Invoice eMail"], ["plain", ""], ["signature", true], ["smtp_server", 8], ["subject", "Factura ${record.number or record.party.name}"], ["to", "${record.party.get_mechanism(''email'') or ''''}"]]'
    );

insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    (
    select distinct on (model)
        id
    from
        electronic_mail_template
    where
        model in (
        select
            id
        from
            ir_model
        where
            model = 'account.invoice'
        )
        ),
    'pyme',
    '[["report", 170], ["template", 4]]',
    'invoice_email_template_report',
    'electronic.mail.template.ir.action.report',
    '[["report", 170], ["template", 4]]'
    );

--
-- Sale
--

insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    (
    select distinct on (model)
        id
    from
        electronic_mail_template
    where
        model in (
        select
            id
        from
            ir_model
        where
            model = 'sale.sale'
        )
        ),
    'pyme',
    '[["engine", "genshi"], ["from_", "user@demo_server.com"], ["html", ""], ["signature", true], ["smtp_server", 8], ["subject", "Pedido"], ["to", "${record.party.email or record.party.get_mechanism(''email'') or ''''}"]]',
    'sale_email_template',
    'electronic.mail.template',
    '[["engine", "genshi"], ["from_", "user@demo_server.com"], ["html", ""], ["signature", true], ["smtp_server", 8], ["subject", "Pedido"], ["to", "${record.party.email or record.party.get_mechanism(''email'') or ''''}"]]'
    );

insert into ir_model_data (create_date, create_uid, noupdate, db_id, module, values, fs_id, model, fs_values)
VALUES (
    '2015-03-03 00:00:00.000000',
    0,
    TRUE,
    (
    select distinct on (model)
        id
    from
        electronic_mail_template
    where
        model in (
        select
            id
        from
            ir_model
        where
            model = 'sale.sale'
        )
        ),
    'pyme',
    '[["report", 170], ["template", 4]]',
    'sale_email_template_report',
    'electronic.mail.template.ir.action.report',
    '[["report", 170], ["template", 4]]'
    );
