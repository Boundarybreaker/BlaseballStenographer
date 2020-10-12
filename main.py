def transcribe(input: str) -> str:
    out = ''
    for i in input:
        if i == '🅰️':
            out += 'A'
        elif i == '🅱️':
            out += 'B'
        elif i == '🅾️':
            out += 'O'
        elif i == 'Ⓜ️':
            out += 'M'
        elif i != '\uFE0F':
            # hooray for multi-character emoji!
            out += chardict.setdefault(i, ' ')
    return out

chardict = {}

default = u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

doublestroke = u'𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫'

negativebox = u'🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉'

positivebox = u'🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉'

bubble = u'ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂ︎ⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ'

fullwidth = u'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'

# unicode's support for small latin capital letters is really weird.
# the Mic only ever uses the tiny high-baseline chars in lowercase,
# so we'll combine both of them here.
tiny = u'ᴀʙᴄᴅᴇꜰɢʜɪᴊᴷʟᴍɴᴏᴘ۹ʀꜱᴛᴜᴠᴡᕽʏᴢᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ'

for i in range(0, 26):
    chardict.update(dict.fromkeys([doublestroke[i], negativebox[i], positivebox[i], bubble[i], fullwidth[i], tiny[i]], default[i]))

for i in range(26, 52):
    chardict.update(dict.fromkeys([doublestroke[i], bubble[i], fullwidth[i], tiny[i]], default[i]))

chardict[' '] = ' '

# returns "TESTING A message FROM THE MIC"
print(transcribe(u'🅃🄴🅂🅃🄸🄽🄶 🅰️ ᵐᵉˢˢᵃᵍᵉ 𝔽ℝ𝕆𝕄 ＴＨＥ Ⓜ️ⒾⒸ'))
