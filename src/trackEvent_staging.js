// Function to get session_id
function getSessionId() {
    function s4() {
        return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);
    }

    if (document.cookie.match(/hk01_session/)) {
        return (document.cookie.match(/hk01_session=([\w\-]+)/)[1]);
    } else {
        var temp_uid = s4() + s4() + "-" + s4() + "-" + s4() + "-" + s4() + "-" + s4() + s4() + s4();
        var d = new Date();
        d.setTime(d.getTime() + (30 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = "hk01_session=" + temp_uid + ";" + expires +
            ";path=/;domain=." + window.location.host.match(/([^\.]+(\.[^\.]+)?)$/)[1];
        return (temp_uid);
    }
}

// Function to get anonymous_id from cookie
function getAnonymousId() {
    function s4() {
        return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);
    }

    if (document.cookie.match(/hk01_annonymous_id/)) {
        return (document.cookie.match(/hk01_annonymous_id=([\w\-]+)/)[1]);
    } else {
        var temp_uid = s4() + s4() + "-" + s4() + "-" + s4() + "-" + s4() + "-" + s4() + s4() + s4();
        var d = new Date();
        d.setTime(d.getTime() + (3650 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = "hk01_annonymous_id=" + temp_uid + ";" + expires +
            ";path=/;domain=." + window.location.host.match(/([^\.]+(\.[^\.]+)?)$/)[1];
        return (temp_uid);
    }
}

// Initialize the tracker client
var myTracker = new trackerClient({
    GA: {
        trackingId: ["UA-70981149-9", "UA-70981149-36", "UA-106000144-1"] // UA-106000144-1 is the profile for hk01data editorial team
    },
    Piwik: {
        trackingUrl: "https://track.hktester.com/v1web/piwik.php",  // replace with your piwik tracking url
        siteId: 5,  // replace with your piwik site ID
        userId: getAnonymousId(), // replace with user ID, should be same as MEMBER_ID/ANONYMOUS_ID
        isSPA: true // if the page is single page application
    }
}, false);

/* Config the selected article detail */
const page_path = "/01偵查/000000/01獨家-整體逾半時間-曬太陽-27幅私人體育會全港互動地圖";
const author = "\u6881\u9038\u98A8, \u6797\u70B3\u5764, \u9673\u4FE1\u7199, \u90B1\u9756\u6C76, \u52DE\u986F\u4EAE, \u6881\u7956\u9952";  // 梁逸風, 林炳坤, 陳信熙, 邱靖汶, 勞顯亮, 梁祖饒
const channel = "01\u5075\u67E5"; // 01偵查
const section = "01\u5075\u67E5"; // 01偵查
const article_id = "000000";

function fireArticlePV(url) {
    try {
        // Send Pageview for article
        myTracker.pageView({
            GA: true,
            Piwik: false
        }, {
                1: author,
                2: section,
                3: channel,
                5: article_id
            }, "https://hk01.com/" + page_path, page_path);

        console.log("fire Article PV");
    }
    catch (err) {
        console.log(err.message);
    }

}

function fireMapPV(url) {
    try {
        myTracker.disableGA({
            'UA-70981149-9': true, // staging
            'UA-106000144-1': true, // hk01 data
            'UA-70981149-36': false // data team 
        });

        // Send Pageview for Map
        myTracker.pageView({
            GA: true,
            Piwik: true
        }, {}, url, removehash(window.location.href).replace(window.location.origin, ''));

        myTracker.resetGAFlags();
        console.log("fire Map PV");
    }
    catch (err) {
        console.log(err.message);
    }

}

function fireEvent(cat, act, lab) {
    try {
        console.log(cat, act, lab);
        myTracker.fire(
            {
                GA: true,
                Piwik: true
            },
            {
                category: cat,
                action: act,
                label: JSON.stringify(lab),
                nonInteraction: false,
                customDimensions: {
                    //[DIMENSION_ARTICLE_AUTHOR]: "Eric"
                }
            }
        );
    }
    catch (err) {
        console.log(err.message);
    }
}

function removehash(string) {
    return string.replace("#", "/");
}