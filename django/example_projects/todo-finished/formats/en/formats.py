# -*- coding: utf-8 -*-
DATETIME_FORMAT = 'N j, Y, P'
SHORT_DATETIME_FORMAT = 'm/d/Y P'
DATE_FORMAT = 'N j, Y'
SHORT_DATE_FORMAT = 'm/d/Y'
TIME_FORMAT = 'P'

DATETIME_INPUT_FORMATS = (
    '%m/%d/%Y %I:%M %p',     # '10/25/2006 02:30 PM'
    '%Y-%m-%d %I:%M %p',     # '2006-10-25 02:30 PM'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
)
DATE_INPUT_FORMATS = (
    '%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d',  # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)
TIME_INPUT_FORMATS = (
    '%I:%M %p',     # '02:30 PM'
    '%H:%M',        # '14:30'
)

# fle 2013-09-02. We aimed to allow entering dates in FR or EN
# but it's complicated because dates are stored as text.
# We should add a column dates_lang to know in which lang dates had been
# entered. For a while : we force 'french' format """
#SCHEDULE_NONWORKINGDAY_FORMAT = '%m/%d'
