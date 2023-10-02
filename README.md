
# Webscraper Microservice [Beta]
Flask API that provides webscraping capabilities for HTML and JavaScript pages using the requests and requests-html libraries in Python.  The API serves as a centralized location for webscraping requests to store logs, optional capabilities (such as adding IP rotating to the container) for high throughput requests, and more.

The repository does not have any examples of IP rotating to obscure requests but services such as <a href="https://oxylabs.io/">Oxylabs</a> or <a href="https://brightdata.com/">Bright Data</a> could be integrated. 

## Installation
### Install requirements.txt first
```
pip install -r requirements.txt
```

## Usage
Expect the response to follow this format:
```json
{
  "message": "Request for webscrape processed.",
  "data": {
    "request": {
      "url": "<insert url scraped here>"
    },
    "response": {
      "status_code": "<insert response from scrape here>",
      "text": "<insert html/js body here>"
    }
  } 
}
```
If using the JavaScript endpoint, a JavaScript selector will need to be provided as it will be used to downselect from webpage.

### Optional - Sleeping Between Scraping:
Within the webscraper.py script, code can be updated, kept, or removed to sleep between requests.  Currently it will pause the scraper for a random amount of time between 2 and 8 seconds.  If the URL is redirected to another URL, the scraper will sleep for a random amount of time between 5-15 seconds.

## Endpoints:

### GET API Help
'GET /help'

**Response**

- '200 OK' on success

```json
{
  "message": "This is an API meant to conduct basic webscraping for standard HTML pages as well as JavaScript using requests_html."
}
```

### GET API Help Single HTML

'GET /help/single/html'

**Response**

- '200 OK' on success

```json
{
  "message": "Given a url, scrape and return the unparsed text off the HTML page."
}
```

### GET API Help JavaScript

'GET /help/single/js'

**Response**

- '200 OK' on success

```json
{
  "message": "Given a url, scrape and return the unparsed text off the JS page."
}
```

### POST HTML Single

'POST /scrape/single/html'

**Request**
```json
{
  "url": "https://www.google.com"
}
```

**Response**
- '200 OK' on success

```json
{
  "data": {
    "request": {
      "url": "https://www.google.com/"
    },
    "response": {
      "status_code": 200,
      "text": "<!doctype html><html itemscope=\"\" itemtype=\"http://schema.org/WebPage\" lang=\"en\"><head><meta content=\"Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.\" name=\"description\"><meta content=\"noodp\" name=\"robots\"><meta content=\"text/html; charset=UTF-8\" http-equiv=\"Content-Type\"><meta content=\"/logos/doodles/2023/celebrating-the-appalachian-trail-6753651837110071.4-l.png\" itemprop=\"image\"><meta content=\"Celebrating the Appalachian Trail \" property=\"twitter:title\"><meta content=\"Celebrating the Appalachian Trail! #GoogleDoodle\" property=\"twitter:description\"><meta content=\"Celebrating the Appalachian Trail! #GoogleDoodle\" property=\"og:description\"><meta content=\"summary_large_image\" property=\"twitter:card\"><meta content=\"@GoogleDoodles\" property=\"twitter:site\"><meta content=\"https://www.google.com/logos/doodles/2023/celebrating-the-appalachian-trail-6753651837110071.2-2xa.gif\" property=\"twitter:image\"><meta content=\"https://www.google.com/logos/doodles/2023/celebrating-the-appalachian-trail-6753651837110071.2-2xa.gif\" property=\"og:image\"><meta content=\"1000\" property=\"og:image:width\"><meta content=\"400\" property=\"og:image:height\"><meta content=\"https://www.google.com/logos/doodles/2023/celebrating-the-appalachian-trail-6753651837110071.2-2xa.gif\" property=\"og:url\"><meta content=\"video.other\" property=\"og:type\"><title>Google</title><script nonce=\"S51RLlFhHrUj_HrYNrBZiw\">(function(){var _g={kEI:'31saZcyGO_Ce5NoPxYqimAs',kEXPI:'0,793108,572360,206,4804,2316,383,246,5,1129120,1197714,687,380090,16114,19398,9286,22430,1362,12319,4746,12834,4998,17075,38444,2872,2891,3926,7828,606,60689,15325,781,1244,1,16916,2652,4,17215,15679,24508,2215,2980,1457,22595,6642,7596,1,11942,30212,2,16395,342,23024,3395,2284,1021,31121,4568,6256,23421,1252,29379,3685,2,2,1,6960,17666,2006,8155,8861,14489,874,9625,10008,7,1922,7834,1945,36285,6174,20198,20137,14,82,13250,1,3263,3692,109,364,2048,5856,18960,2305,3098,3030,5629,10187,1804,7734,15103,2995,7265,2172,960,4292,6561,1632,8842,17859,7915,9395,8759,3592,5210031,108,2,195,576,5994193,98,2803117,3311,141,795,28559,537,8856003,15085468,398,4043709,16673,36925,358,1999,176,4424,3,688,1395366,338513,23420757,4117,4046,4636,8408,2093,787,44,290,108,1155,1085,2466,873,1854,2767,1178,1966,3163,1173,9,24,3649,448,2962,2979,2223,820,872,1,1,2,3,2817,3447,316,1019,2098,3999,1879,849,674,1713,294,49,2785,1879,5260,1591,989,152,923,1299,582,1519,4546,1,2,1044,2219,2258,40,315,198,9,2739,612,378,2,17,59,1745,652,575,169,195,877,598,1,1,2,3,509,546,2,631,346,620,3,526,195,60,6,1718,3,1662,213,94,1,10,215,614,473,283,7,1,8,154,684,4,409,464,4,865,107,876,1,14,93,687,9,18,28,2,76,4,91,77,790,939,2,19,3,698,271,37,1226,68,5,454,2,7,1,508,182,446,113,251,7,1,8,785,16,404,99,975,1,850,722,599,32,327,3,46,12,49,203,1,543,1,76,103,2,89,302,496,4,4,10,964,8,455,5,979,630,3,80,25,1,371,912,1,64,413,313,76,1019,42',kBL:'04ye',kOPI:89978449};(function(){var a;(null==(a=window.google)?0:a.stvsc)?google.kEI=_g.kEI:window.google=_g;}).call(this);})();(function(){google.sn='webhp';google.kHL='en';})();(function(){\nvar h=this||self;function l(){return void 0!==window.google&&void 0!==window.google.kOPI&&0!==window.google.kOPI?window.google.kOPI:null};var m,n=[];function p(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute(\"eid\")));)a=a.parentNode;return b||m}function q(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute(\"leid\")));)a=a.parentNode;return b}function r(a){/^http:/i.test(a)&&\"https:\"===window.location.protocol&&(google.ml&&google.ml(Error(\"a\"),!1,{src:a,glmm:1}),a=\"\");return a}\nfunction t(a,b,c,d,k){var e=\"\";-1===b.search(\"&ei=\")&&(e=\"&ei=\"+p(d),-1===b.search(\"&lei=\")&&(d=q(d))&&(e+=\"&lei=\"+d));d=\"\";var g=-1===b.search(\"&cshid=\")&&\"slh\"!==a,f=[];f.push([\"zx\",Date.now().toString()]);h._cshid&&g&&f.push([\"cshid\",h._cshid]);c=c();null!=c&&f.push([\"opi\",c.toString()]);for(c=0;c<f.length;c++){if(0===c||0<c)d+=\"&\";d+=f[c][0]+\"=\"+f[c][1]}return\"/\"+(k||\"gen_204\")+\"?atyp=i&ct=\"+String(a)+\"&cad=\"+(b+e+d)};m=google.kEI;google.getEI=p;google.getLEI=q;google.ml=function(){return null};google.log=function(a,b,c,d,k,e){e=void 0===e?l:e;c||(c=t(a,b,e,d,k));if(c=r(c)){a=new Image;var g=n.length;n[g]=a;a.onerror=a.onload=a.onabort=function(){delete n[g]};a.src=c}};google.logUrl=function(a,b){b=void 0===b?l:b;return t(\"\",a,b)};}).call(this);(function(){google.y={};google.sy=[];google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.sx=function(a){google.sy.push(a)};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};google.bx=!1;google.lx=function(){};var d=[];google.fce=function(a,b,c,e){d.push([a,b,c,e])};google.qce=d;}).call(this);google.f={};(function(){\ndocument.documentElement.addEventListener(\"submit\",function(b){var a;if(a=b.target){var c=a.getAttribute(\"data-submitfalse\");a=\"1\"===c||\"q\"===c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener(\"click\",function(b){var a;a:{for(a=b.target;a&&a!==document.documentElement;a=a.parentElement)if(\"A\"===a.tagName){a=\"1\"===a.getAttribute(\"data-nohref\");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\n</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#1967d2}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#681da8;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#1967d2}a:visited{color:#681da8}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#f8f9fa;border:solid 1px;border-color:#dadce0 #70757a #70757a #dadce0;height:30px}.lsbb{display:block}#WqQANb a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;color:#000;border:none;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#dadce0}.lst:focus{outline:none}</style><script nonce=\"S51RLlFhHrUj_HrYNrBZiw\">(function(){window.google.erd={jsr:1,bv:1874,de:true};\nvar h=this||self;var k,l=null!=(k=h.mei)?k:1,n,p=null!=(n=h.sdo)?n:!0,q=0,r,t=google.erd,v=t.jsr;google.ml=function(a,b,d,m,e){e=void 0===e?2:e;b&&(r=a&&a.message);void 0===d&&(d={});d.cad=\"ple_\"+google.ple+\".aple_\"+google.aple;if(google.dl)return google.dl(a,e,d),null;if(0>v){window.console&&console.error(a,d);if(-2===v)throw a;b=!1}else b=!a||!a.message||\"Error loading script\"===a.message||q>=l&&!m?!1:!0;if(!b)return null;q++;d=d||{};b=encodeURIComponent;var c=\"/gen_204?atyp=i&ei=\"+b(google.kEI);google.kEXPI&&(c+=\"&jexpid=\"+b(google.kEXPI));c+=\"&srcpg=\"+b(google.sn)+\"&jsr=\"+b(t.jsr)+\"&bver=\"+\nb(t.bv);var f=a.lineNumber;void 0!==f&&(c+=\"&line=\"+f);var g=a.fileName;g&&(0<g.indexOf(\"-extension:/\")&&(e=3),c+=\"&script=\"+b(g),f&&g===window.location.href&&(f=document.documentElement.outerHTML.split(\"\\n\")[f],c+=\"&cad=\"+b(f?f.substring(0,300):\"No script found.\")));google.ple&&1===google.ple&&(e=2);c+=\"&jsel=\"+e;for(var u in d)c+=\"&\",c+=b(u),c+=\"=\",c+=b(d[u]);c=c+\"&emsg=\"+b(a.name+\": \"+a.message);c=c+\"&jsst=\"+b(a.stack||\"N/A\");12288<=c.length&&(c=c.substr(0,12288));a=c;m||google.log(0,\"\",a);return a};window.onerror=function(a,b,d,m,e){r!==a&&(a=e instanceof Error?e:Error(a),void 0===d||\"lineNumber\"in a||(a.lineNumber=d),void 0===b||\"fileName\"in a||(a.fileName=b),google.ml(a,!1,void 0,!1,\"SyntaxError\"===a.name||\"SyntaxError\"===a.message.substring(0,11)||-1!==a.message.indexOf(\"Script error\")?3:0));r=null;p&&q>=l&&(window.onerror=null)};})();</script></head><body bgcolor=\"#fff\"><script nonce=\"S51RLlFhHrUj_HrYNrBZiw\">(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\n}\n})();</script><div id=\"mngb\"><div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href=\"https://www.google.com/imghp?hl=en&tab=wi\">Images</a> <a class=gb1 href=\"https://maps.google.com/maps?hl=en&tab=wl\">Maps</a> <a class=gb1 href=\"https://play.google.com/?hl=en&tab=w8\">Play</a> <a class=gb1 href=\"https://www.youtube.com/?tab=w1\">YouTube</a> <a class=gb1 href=\"https://news.google.com/?tab=wn\">News</a> <a class=gb1 href=\"https://mail.google.com/mail/?tab=wm\">Gmail</a> <a class=gb1 href=\"https://drive.google.com/?tab=wo\">Drive</a> <a class=gb1 style=\"text-decoration:none\" href=\"https://www.google.com/intl/en/about/products?tab=wh\"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href=\"http://www.google.com/history/optout?hl=en\" class=gb4>Web History</a> | <a  href=\"/preferences?hl=en\" class=gb4>Settings</a> | <a target=_top id=gb_70 href=\"https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ\" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div></div><center><br clear=\"all\" id=\"lgpd\"><div id=\"lga\"><a href=\"/search?sca_esv=569950492&amp;ie=UTF-8&amp;q=Appalachian+Trail+&amp;oi=ddle&amp;ct=258248615&amp;hl=en&amp;si=ALGXSlZS0YT-iRe81F2cKC9lM9KWTK4y0m5Atx8g9YliNNw2mdrEYzQlmBMLnd9qYZl96JCBoB6JvMTobLGvePyDgibBW_WUOGKORF4uporwGLeikpr6REQIB6MY2QL8xeN-bqqtjv7Vfa0O8QaXyw78UcwK-6-pw9fCvvhnDyPTrMUXP4R05-g%3D&amp;sa=X&amp;ved=0ahUKEwiM8pij19aBAxVwD1kFHUWFCLMQPQgD\"><img alt=\"Celebrating the Appalachian Trail \" border=\"0\" height=\"200\" src=\"/logos/doodles/2023/celebrating-the-appalachian-trail-6753651837110071.4-l.png\" title=\"Celebrating the Appalachian Trail \" width=\"500\" id=\"hplogo\"><br></a><br></div><form action=\"/search\" name=\"f\"><table cellpadding=\"0\" cellspacing=\"0\"><tr valign=\"top\"><td width=\"25%\">&nbsp;</td><td align=\"center\" nowrap=\"\"><input name=\"ie\" value=\"ISO-8859-1\" type=\"hidden\"><input value=\"en\" name=\"hl\" type=\"hidden\"><input name=\"source\" type=\"hidden\" value=\"hp\"><input name=\"biw\" type=\"hidden\"><input name=\"bih\" type=\"hidden\"><div class=\"ds\" style=\"height:32px;margin:4px 0\"><input class=\"lst\" style=\"margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000\" autocomplete=\"off\" value=\"\" title=\"Google Search\" maxlength=\"2048\" name=\"q\" size=\"57\"></div><br style=\"line-height:0\"><span class=\"ds\"><span class=\"lsbb\"><input class=\"lsb\" value=\"Google Search\" name=\"btnG\" type=\"submit\"></span></span><span class=\"ds\"><span class=\"lsbb\"><input class=\"lsb\" id=\"tsuid_1\" value=\"I'm Feeling Lucky\" name=\"btnI\" type=\"submit\"><script nonce=\"S51RLlFhHrUj_HrYNrBZiw\">(function(){var id='tsuid_1';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}\nelse top.location='/doodles/';};})();</script><input value=\"AO6bgOgAAAAAZRpp74Naba63eWOkHxogZxhHcRIWOOkO\" name=\"iflsig\" type=\"hidden\"></span></span></td><td class=\"fl sblc\" align=\"left\" nowrap=\"\" width=\"25%\"><a href=\"/advanced_search?hl=en&amp;authuser=0\">Advanced search</a></td></tr></table><input id=\"gbv\" name=\"gbv\" type=\"hidden\" value=\"1\"><script nonce=\"S51RLlFhHrUj_HrYNrBZiw\">(function(){var a,b=\"1\";if(document&&document.getElementById)if(\"undefined\"!=typeof XMLHttpRequest)b=\"2\";else if(\"undefined\"!=typeof ActiveXObject){var c,d,e=[\"MSXML2.XMLHTTP.6.0\",\"MSXML2.XMLHTTP.3.0\",\"MSXML2.XMLHTTP\",\"Microsoft.XMLHTTP\"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b=\"2\"}catch(h){}}a=b;if(\"2\"==a&&-1==location.search.indexOf(\"&gbv=2\")){var f=google.gbvu,g=document.getElementById(\"gbv\");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id=\"gac_scont\"></div><div style=\"font-size:83%;min-height:3.5em\"><br></div><span id=\"footer\"><div style=\"font-size:10pt\"><div style=\"margin:19px auto;text-align:center\" id=\"WqQANb\"><a href=\"/intl/en/ads/\">Advertising</a><a href=\"/services/\">Business Solutions</a><a href=\"/intl/en/about.html\">About Google</a></div></div><p style=\"font-size:8pt;color:#70757a\">&copy; 2023 - <a href=\"/intl/en/policies/privacy/\">Privacy</a> - <a href=\"/intl/en/policies/terms/\">Terms</a></p></span></center><script nonce=\"S51RLlFhHrUj_HrYNrBZiw\">(function(){window.google.cdo={height:757,width:1440};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d=\"CSS1Compat\"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}\nif(a&&b&&(a!=google.cdo.width||b!=google.cdo.height)){var e=google,f=e.log,g=\"/client_204?&atyp=i&biw=\"+a+\"&bih=\"+b+\"&ei=\"+google.kEI,h=\"\",k=[],l=void 0!==window.google&&void 0!==window.google.kOPI&&0!==window.google.kOPI?window.google.kOPI:null;null!=l&&k.push([\"opi\",l.toString()]);for(var m=0;m<k.length;m++){if(0===m||0<m)h+=\"&\";h+=k[m][0]+\"=\"+k[m][1]}f.call(e,\"\",\"\",g+h)};}).call(this);})();</script> <script nonce=\"S51RLlFhHrUj_HrYNrBZiw\">(function(){google.xjs={ck:'xjs.hp.g9ge3mf3C4Q.L.X.O',cs:'ACT90oEp89useno9mNOqaMOCtdvjurDWVQ',cssopt:false,csss:'ACT90oGW_1Frq_UUisHYr47oYrkMgCQ7DQ',excm:[],sepcss:false};})();</script>     <script nonce=\"S51RLlFhHrUj_HrYNrBZiw\">(function(){var u='/xjs/_/js/k\\x3dxjs.hp.en.ZIe9CU6whKs.O/am\\x3dAAAAAAAAAAAAAAAAgAAAAAAAUABAgAAAAAAAAAAABACgIwAAFgDgAg/d\\x3d1/ed\\x3d1/rs\\x3dACT90oH8e2neK9xqdfqo9Pm3AyEkqwZeJQ/m\\x3dsb_he,d,cEt90b,SNUn3,qddgKe,sTsDMc,dtl0hd,eHDfl';var amd=0;\nvar e=this||self,f=function(a){return a};var g;var h=function(a){this.g=a};h.prototype.toString=function(){return this.g+\"\"};var k={};var l=function(){var a=document;var b=\"SCRIPT\";\"application/xhtml+xml\"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)};\nfunction m(a,b){a.src=b instanceof h&&b.constructor===h?b.g:\"type_error:TrustedResourceUrl\";var c,d;(c=(b=null==(d=(c=(a.ownerDocument&&a.ownerDocument.defaultView||window).document).querySelector)?void 0:d.call(c,\"script[nonce]\"))?b.nonce||b.getAttribute(\"nonce\")||\"\":\"\")&&a.setAttribute(\"nonce\",c)};function n(a){a=null===a?\"null\":void 0===a?\"undefined\":a;if(void 0===g){var b=null;var c=e.trustedTypes;if(c&&c.createPolicy){try{b=c.createPolicy(\"goog#html\",{createHTML:f,createScript:f,createScriptURL:f})}catch(d){e.console&&e.console.error(d.message)}g=b}else g=b}a=(b=g)?b.createScriptURL(a):a;return new h(a,k)};void 0===google.ps&&(google.ps=[]);function p(){var a=u,b=function(){};google.lx=google.stvsc?b:function(){q(a);google.lx=b};google.bx||google.lx()}function r(a,b){b&&m(a,n(b));var c=a.onload;a.onload=function(d){c&&c(d);google.ps=google.ps.filter(function(t){return a!==t})};google.ps.push(a);document.body.appendChild(a)}google.as=r;function q(a){google.timers&&google.timers.load&&google.tick&&google.tick(\"load\",\"xjsls\");var b=l();b.onerror=function(){google.ple=1};b.onload=function(){google.ple=0};google.xjsus=void 0;r(b,a);google.aple=-1;google.psa=!0};google.xjsu=u;e._F_jsUrl=u;setTimeout(function(){0<amd?google.caft(function(){return p()},amd):p()},0);})();window._ = window._ || {};window._DumpException = _._DumpException = function(e){throw e;};window._s = window._s || {};_s._DumpException = _._DumpException;window._qs = window._qs || {};_qs._DumpException = _._DumpException;(function(){window._F_toggles=[1,0,0,8192,268436480,33619969,0,2048,597688324,5767168,11776];})();function _F_installCss(c){}\n(function(){google.jl={blt:'none',chnk:0,dw:false,dwu:true,emtn:0,end:0,ico:false,ikb:0,ine:false,injs:'none',injt:0,injth:0,injv2:false,lls:'default',pdt:0,rep:0,snet:true,strt:0,ubm:false,uwp:true};})();(function(){var pmc='{\\x22d\\x22:{},\\x22sb_he\\x22:{\\x22agen\\x22:true,\\x22cgen\\x22:true,\\x22client\\x22:\\x22heirloom-hp\\x22,\\x22dh\\x22:true,\\x22ds\\x22:\\x22\\x22,\\x22fl\\x22:true,\\x22host\\x22:\\x22google.com\\x22,\\x22jsonp\\x22:true,\\x22msgs\\x22:{\\x22cibl\\x22:\\x22Clear Search\\x22,\\x22dym\\x22:\\x22Did you mean:\\x22,\\x22lcky\\x22:\\x22I\\\\u0026#39;m Feeling Lucky\\x22,\\x22lml\\x22:\\x22Learn more\\x22,\\x22psrc\\x22:\\x22This search was removed from your \\\\u003Ca href\\x3d\\\\\\x22/history\\\\\\x22\\\\u003EWeb History\\\\u003C/a\\\\u003E\\x22,\\x22psrl\\x22:\\x22Remove\\x22,\\x22sbit\\x22:\\x22Search by image\\x22,\\x22srch\\x22:\\x22Google Search\\x22},\\x22ovr\\x22:{},\\x22pq\\x22:\\x22\\x22,\\x22rfs\\x22:[],\\x22sbas\\x22:\\x220 3px 8px 0 rgba(0,0,0,0.2),0 0 0 1px rgba(0,0,0,0.08)\\x22,\\x22stok\\x22:\\x22VVnVKfQY-sHpZNrqrB1aoMcN7u4\\x22}}';google.pmc=JSON.parse(pmc);})();(function(){var b=function(a){var c=0;return function(){return c<a.length?{done:!1,value:a[c++]}:{done:!0}}};\nvar e=this||self;var g,h;a:{for(var k=[\"CLOSURE_FLAGS\"],l=e,n=0;n<k.length;n++)if(l=l[k[n]],null==l){h=null;break a}h=l}var p=h&&h[610401301];g=null!=p?p:!1;var q,r=e.navigator;q=r?r.userAgentData||null:null;function t(a){return g?q?q.brands.some(function(c){return(c=c.brand)&&-1!=c.indexOf(a)}):!1:!1}function u(a){var c;a:{if(c=e.navigator)if(c=c.userAgent)break a;c=\"\"}return-1!=c.indexOf(a)};function v(){return g?!!q&&0<q.brands.length:!1}function w(){return u(\"Safari\")&&!(x()||(v()?0:u(\"Coast\"))||(v()?0:u(\"Opera\"))||(v()?0:u(\"Edge\"))||(v()?t(\"Microsoft Edge\"):u(\"Edg/\"))||(v()?t(\"Opera\"):u(\"OPR\"))||u(\"Firefox\")||u(\"FxiOS\")||u(\"Silk\")||u(\"Android\"))}function x(){return v()?t(\"Chromium\"):(u(\"Chrome\")||u(\"CriOS\"))&&!(v()?0:u(\"Edge\"))||u(\"Silk\")}function y(){return u(\"Android\")&&!(x()||u(\"Firefox\")||u(\"FxiOS\")||(v()?0:u(\"Opera\"))||u(\"Silk\"))};var z=v()?!1:u(\"Trident\")||u(\"MSIE\");y();x();w();var A=!z&&!w(),D=function(a){if(/-[a-z]/.test(\"ved\"))return null;if(A&&a.dataset){if(y()&&!(\"ved\"in a.dataset))return null;a=a.dataset.ved;return void 0===a?null:a}return a.getAttribute(\"data-\"+\"ved\".replace(/([A-Z])/g,\"-$1\").toLowerCase())};var E=[],F=null;function G(a){a=a.target;var c=performance.now(),f=[],H=f.concat,d=E;if(!(d instanceof Array)){var m=\"undefined\"!=typeof Symbol&&Symbol.iterator&&d[Symbol.iterator];if(m)d=m.call(d);else if(\"number\"==typeof d.length)d={next:b(d)};else throw Error(\"a`\"+String(d));for(var B=[];!(m=d.next()).done;)B.push(m.value);d=B}E=H.call(f,d,[c]);if(a&&a instanceof HTMLElement)if(a===F){if(c=4<=E.length)c=5>(E[E.length-1]-E[E.length-4])/1E3;if(c){c=google.getEI(a);a.hasAttribute(\"data-ved\")?f=a?D(a)||\"\":\"\":f=(f=\na.closest(\"[data-ved]\"))?D(f)||\"\":\"\";f=f||\"\";if(a.hasAttribute(\"jsname\"))a=a.getAttribute(\"jsname\");else{var C;a=null==(C=a.closest(\"[jsname]\"))?void 0:C.getAttribute(\"jsname\")}google.log(\"rcm\",\"&ei=\"+c+\"&ved=\"+f+\"&jsname=\"+(a||\"\"))}}else F=a,E=[c]}window.document.addEventListener(\"DOMContentLoaded\",function(){document.body.addEventListener(\"click\",G)});}).call(this);</script></body></html>"
    }
  },
  "message": "Request for webscrape processed."
}
```

### POST JavaScript Single

'POST /scrape/single/js'

**Request**
```json
{
  "url": "https://www.reuters.com/business/autos-transportation/japan-puts-brakes-lucrative-used-car-trade-with-russia-2023-10-01/",
  "selector": "#fusion-metadata"
}
```

**Response**
- '200 OK' on success

```json
{
  "data": {
    "request": {
      "url": "https://www.reuters.com/business/autos-transportation/japan-puts-brakes-lucrative-used-car-trade-with-russia-2023-10-01/"
    },
    "response": {
      "status_code": 200,
      "text": "window.Fusion=window.Fusion||{};Fusion.arcSite=\"reuters\";Fusion... ... ..."
    }
  }
}
```