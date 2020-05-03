from app import db
from app.models import News

a = News(title='Apple iPhone XS 勁劈至 HK＄3899！抵玩過 iPhone SE？',
         content='Apple iPhone SE 推出僅 1 星期，在中價機市場大受歡迎。不過今次有電訊商將 iPhone XS 系列全綫劈價，HK$3,899 就有 iPhone XS，雖然 CPU 係 Apple 上一代的 A12，但擁有雙鏡頭、Face ID、更靚嘅屏幕等，吸引度極高！。')
b = News(title='Samsung 正開發 2 億像素感光元件！預計明年初推出',
         content='繼小米和 Samsung 之後，今年陸續有更多手機採用 1 億拍攝像素鏡頭，智能手機的相片像素不斷提升，早前 Samsung 更表示打算開發出超越人眼極限的 6 億像素感光元件，相當誇張，不過在 6 億像素感光元件推出之前，有消息指 Samsung 已經正在開發 2.5 億像素感光元件，並預計來年初就會正式使用。。')
c = News(title='Intel 十代 Core 正式登場！最高 10 核心‧5.3GHz Turbo 時脈',
         content='Intel 主流桌面 (Mainstream Desktop) 第十代 Core 處理器，代號「Comet Lake-S」，終於在香港時間 4 月 30 日 9pm 全球正式公布，LGA1,200 插座新世代來了！Comet Lake-S 最高 10 核心、14nm+++ 改良版製程、配以全新 400 系列晶片等。根據 Intel 規定，暫時全球媒體只能透露第十代 Core 平台的技術細節，待到香港時間 5 月 20 日 9pm 後才可公開效能數據，產品亦於當天全球上市！')
d = News(title='微軟推 Win 10 更新 大幅提升硬碟效能',
         content='微軟 Microsoft 每月都會為 Windows 用戶推送更新，以修補作系統問題，但通常用戶都沒有特別感覺。不過，在即將推出的 5 月更新，大家可能會感覺系統速度變快，由其是使用傳統硬碟的電腦。')
e = News(title='不受新冠肺炎疫情影響 高通：5G發布如常',
         content='在 5G 設備陸續發布下，高通（Qualcomm）預計在 2020 年內每塊晶片的利潤可大幅上升。該公司預計，2020 年度內 5G 手機出貨量可達最多 2.25 億部，更認為就算新冠肺炎疫情持續，也不會減慢主要地區的 5G 建網與裝置發布速度。。')
f = News(title='Intel被淡出？傳明年出貨Mac機改用自家處理器',
         content='《彭博》(Bloomberg）引述消息，指蘋果（Apple）計劃 2021 年起，在最少 1 款 Mac 電腦中採用自家處理器，這意味著該公司與英特爾（Intel）自 2006 年以來的獨家合作，有機會開始走向結局。。')
g = News(title='VMware：加速改造應用 K8s 普及在望',
         content='數碼轉型已席捲全球，VMware 香港及澳門總經理藍建基指出，特別在新冠肺炎疫情下網上服務推出時間更急。 在這情況下原生雲（Native Cloud）也能配合而生。隨著全球原生雲市場不斷成長， Gartner 也預計 K8s 會用於 80% 的雲端平台中。他指出 VMware 是目前全球第二大的 K8s 技術貢獻機構，地位僅次於 Google。')
h = News(title='Wi-Fi 6E登場 增1.2 GHz可用頻寬',
         content='美國聯邦通訊委員會（FCC）早前投票通過「Wi-Fi 6E」標準，當中最重要的決定是開放 6GHz 範圍的白色頻段（White Space）給公眾使用，將會額外提供 1,200MHz 頻寬，相比現時 5GHz 範圍的 500Mhz，與 2.4GHz 的 60MHz 大為提升。。')
db.session.add(a)
db.session.add(b)
db.session.add(c)
db.session.add(d)
db.session.add(e)
db.session.add(f)
db.session.add(g)
db.session.add(h)
db.session.commit()
