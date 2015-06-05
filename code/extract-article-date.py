RX_MONTHS_SHORT = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept?|Oct|Nov|Dec\.?"
RX_MONTHS_FULL = "January|February|March|April|May|June|July|August|September|October|November|December"
RX_DAYS_SHORT = "Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday"
RX_DAYS_FULL = "Mon|Tues?|Weds?|Thu(?:rs?)?|Fri|Sat|Sun"


RX_DATETIME_FORMATS = [
  "", # 2015-06-11
  "", # 6-11-[20]15 (U.S.)
  "", # 11-6-[20]15 (Non-U.S.)
  "", # 6/11/[20]15 (U.S.)
  "", # 11/6/[20]15 (Non-U.S.)
  "", # Thurs[day], June 11[, 2015]
]



# DATETIME_REGEXEN = [
#   /#{MONTHS_REGEX}\b\s+\d+\D{1,10}\d{4}/i/,
#   /(on\s+)?\d+\s+#{MONTHS_REGEX}\s+\D{0,10}\d+/i,
#   /(on[^\d+]{1,10})\d+(th|st|rd)?.{1,10}#{MONTHS_REGEX}\b[^\d]{1,10}\d+/i,
#   /\b\d{4}\-\d{2}\-\d{2}\b/i,
#   /\d+(th|st|rd).{1,10}#{MONTHS_REGEX}\b[^\d]{1,10}\d+/i,
#   /\d+\s+#{MONTHS_REGEX}\b[^\d]{1,10}\d+/i,
#   /on\s+#{MONTHS_REGEX}\s+\d+/i,
#   /#{MONTHS_REGEX}\s+\d+/i,
#   /\d{4}[\.\/\-]\d{2}[\.\/\-]\d{2}/,
#   /\d{2}[\.\/\-]\d{2}[\.\/\-]\d{4}/
# ]

