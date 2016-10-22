# -*- coding: utf-8 -*-
DATETIME_FORMAT = 'd F Y à H:i'
SHORT_DATETIME_FORMAT = 'd/m/Y H:i'
DATE_FORMAT = 'd F Y'
SHORT_DATE_FORMAT = 'd b Y'
TIME_FORMAT = 'H:i'

DATETIME_INPUT_FORMATS = ('%d/%m/%Y %H:%M', '%d/%m/%Y')
DATE_INPUT_FORMATS = ('%d/%m/%Y', )
TIME_INPUT_FORMATS = ('%H:%M', )

# Needed for form tests
#DATE_INPUT_FORMATS += ('%Y-%m-%d', )
#DATETIME_INPUT_FORMATS += ('%Y-%m-%d %H:%M', )

# fle 2013-09-02. We aimed to allow entering dates in FR or EN
# but it's complicated because dates are stored as text.
# We should add a column dates_lang to know in which lang dates had been
# entered. For a while : we force 'french' format """
#SCHEDULE_NONWORKINGDAY_FORMAT = '%d/%m'
