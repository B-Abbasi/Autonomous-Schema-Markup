class XMLPatterns:
  regExpressions= {
    "personName":re.compile(r"(&lt;PersonName&gt;)(.*?)(&lt;/PersonName&gt;)"),
    "title":re.compile(r"(&lt;Title&gt;)(.*?)(&lt;/Title&gt;)"),
    "address":re.compile(r"(&lt;Address&gt;)(.*?)(&lt;/Address&gt;)"),
    "email":re.compile(r"(&lt;EMail&gt;)(.*?)(&lt;/EMail&gt;)"),
    "organization":re.compile(r"(&lt;Organization&gt;)(.*?)(&lt;/Organization&gt;)"),
    "institute":re.compile(r"(&lt;Institute&gt;)(.*?)(&lt;/Institute&gt;)"),
    "department":re.compile(r"(&lt;Department&gt;)(.*?)(&lt;/Department&gt;)"),
    "instituteName":re.compile(r"(&lt;InstituteName&gt;)(.*?)(&lt;/InstituteName&gt;)"),
    "url":re.compile(r"(&lt;url&gt;)(.*?)(&lt;/url&gt;)"),
    "contact":re.compile(r"(&lt;Contact&gt;)(.*?)(&lt;/Contact&gt;)"),
    "qualification":re.compile(r"(&lt;Qualification&gt;)(.*?)(&lt;/Qualification&gt;)"),
    "domain":re.compile(r"(&lt;Domain&gt;)(.*?)(&lt;/Domain&gt;)") 
            }
 
  entityIdentifier= {
    "personName":" PN ",
    "title":" TTL ",
    "address":" ADRS ",
    "email":" EMAIL ",
    "organization":" ORG ",
    "institute":" INSTUT ",
    "department":" DEPT ",
    "instituteName":" INSTUT ",
    "url":" URL ",
    "contact":" CONTACT ",
    "qualification":" QUAL ",
    "domain":" DOMAIN "
            }