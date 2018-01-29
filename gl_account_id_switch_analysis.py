lendapi\accounting\csv_utils.py (17 hits)
	Line 95:                                                         gl_account_id=line[2]).first()
	Line 98:                                                        gl_account_id=line[2],
    
                                  # could use variable in company meta instead of Max to fix this entire block
	Line 123:                     c = CoA.objects.filter(company=company).aggregate(Max('gl_account_id'))
	Line 129:                     if c['gl_account_id__max']:
	Line 130:                         gl_acct_id = int(c['gl_account_id__max']) + 1
	Line 137:                                            gl_account_id=gl_acct_id,
                                  #####################################################
                                  
	Line 162:                 'gl_account_id': '',
	Line 168:                 'gl_account_id': 2,
	Line 210:                 exists = TrialBalance.objects.filter(period=period_ending, gl_account_id=line[0], company=company).first()
	Line 218:                                                     gl_account_id=line[0],
	Line 258:                 gl_account_id = AccountingUtils.get_gl_account_id_by_name(company, line[0])
	Line 258:                 gl_account_id = AccountingUtils.get_gl_account_id_by_name(company, line[0])
	Line 259:                 print('account id is ', gl_account_id)
	Line 261:                                                      gl_account_id=gl_account_id,
	Line 261:                                                      gl_account_id=gl_account_id,
	Line 271:                                                     gl_account_id=gl_account_id,
	Line 271:                                                     gl_account_id=gl_account_id,

lendapi\accounting\models.py (2 hits)
	Line 39:     gl_account_id = models.IntegerField(blank=True, null=True)
	Line 76:     gl_account_id = models.IntegerField(null=True, blank=True)
    
    
lendapi\accounting\utils.py (6 hits)
	Line 182:                     "AccountId": str(entry.gl_account_id),
	Line 193:                 "AccountId": str(coa.gl_account_id),
    
                              # cust_account_id also needs to be changed to varchar
	Line 221:                 exists = CoAMap.objects.filter(company=company, cust_account_id=account.gl_account_id).first()
	Line 225:                                      cust_account_id=account.gl_account_id,
                              #########################
                              
	Line 250:     def get_gl_account_id_by_name(company, account_name):
	Line 255:             gl_id = coa.gl_account_id
    
    
lendapi\v1\accounting\qbo\utils.py (5 hits)
	Line 41:             exists = CoA.objects.filter(company=company, gl_account_id=account["Id"]).first()
	Line 45:                 exists.gl_account_id = account["Id"]
	Line 53:                           gl_account_id=account["Id"], gl_account_bal=account["CurrentBalance"])
	Line 86:                                                          gl_account_id=d["id"],
	Line 96:                                              gl_account_id=d["id"])
    
    
lendapi\v1\accounting\serializers.py (2 hits)
	Line 57:         fields = ('company', 'gl_account_id', 'gl_account_name', 'gl_account_type', 'gl_account_bal', 'gl_account_currency')
	Line 66:         fields = ('company', 'gl_account_name', 'gl_account_id', 'debit', 'credit', 'period', 'currency')
    
    
lendapi\accounting\csv_utils.py (17 hits)
	Line 95:                                                         gl_account_id=line[2]).first()
	Line 98:                                                        gl_account_id=line[2],
	Line 123:                     c = CoA.objects.filter(company=company).aggregate(Max('gl_account_id'))
	Line 129:                     if c['gl_account_id__max']:
	Line 130:                         gl_acct_id = int(c['gl_account_id__max']) + 1
	Line 137:                                            gl_account_id=gl_acct_id,
	Line 162:                 'gl_account_id': '',
	Line 168:                 'gl_account_id': 2,
	Line 210:                 exists = TrialBalance.objects.filter(period=period_ending, gl_account_id=line[0], company=company).first()
	Line 218:                                                     gl_account_id=line[0],
	Line 258:                 gl_account_id = AccountingUtils.get_gl_account_id_by_name(company, line[0])
	Line 258:                 gl_account_id = AccountingUtils.get_gl_account_id_by_name(company, line[0])
	Line 259:                 print('account id is ', gl_account_id)
	Line 261:                                                      gl_account_id=gl_account_id,
	Line 261:                                                      gl_account_id=gl_account_id,
	Line 271:                                                     gl_account_id=gl_account_id,
	Line 271:                                                     gl_account_id=gl_account_id,

    
lendapi\accounting\utils.py (6 hits)
	Line 182:                     "AccountId": str(entry.gl_account_id),
	Line 193:                 "AccountId": str(coa.gl_account_id),
	Line 221:                 exists = CoAMap.objects.filter(company=company, cust_account_id=account.gl_account_id).first()
	Line 225:                                      cust_account_id=account.gl_account_id,
	Line 250:     def get_gl_account_id_by_name(company, account_name):
	Line 255:             gl_id = coa.gl_account_id
