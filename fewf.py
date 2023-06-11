import vk_api
import random
from cb_rf import get_dollar_course 
vk = vk_api.VkApi(token="vk1.a.pZGRKmb-OM-xiNTWy9f6Mi-6B7mTxYYD8X9czrScKRXLaPtVHuL-fa51h7cxvi7uobxX7_1BxfTXg6Mv5S2Vziwancy_Ly0u1m3AuL5C69wD2m-f92tOUIHFv_WypvaAo_lTbQKrBCR2HEwW7KPrrCboHv72-hSgqj0O-Ycmi7SmNN5DCM2dEhy1zu_Dgt64S2__6tqddThgq6sWcp1DPA")




while True :
    messages = vk.method("messages.getConversations", {"count ":20 , "filter": "unanswered"})
    if messages["count"] >=1:
        msg_text = messages["items"][0]["last_message"]["text"]
        user_id = messages ["items"][0]["last_message"]["from_id"]


        if msg_text.lower() == "курс":
            ans = f"курс доллара на сегосдня составляет {get_dollar_course()}руб. "
        else :
            ans = "неизвестная команда"

        vk.method("messages.send",{'random_id': random.randint(-10**7 , 10**7),'user_id'  : user_id   ,'message'  : msg_text})
     

        