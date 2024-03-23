import os

os.chdir("/Users/osadamasashi/Desktop/ossa2019.stars.ne.jp")


class myHtml:
    def __init__(self, html=None, file=None):
        if(file != None):
            self.read(file)
        else:
            self.html = html
        self.read_depth = 0
        self.write_depth = 0
        self.tab_space = " "*4
        self.list_ = list()
        
        self.blog_depth = "../"
        
        self.version = "1.4"
    
    
    def set_file(self, read, write):
        self.read(read)
        self.read_file = read
        self.write_file = write
        self.read_depth = self.get_depth(read)
        self.write_depth = self.get_depth(write)
    
        
    def get_depth(self, file):
        depth = file.count("/")
        return depth, "../"*depth
    
    
    # over ride
    def replace(self, before, after):
        before = before.replace("___t___", self.tab_space)
        after = after.replace("___t___", self.tab_space)
        self.html = self.html.replace(before, after)
    
    
    def delete(self, xs):
        xs = xs.replace("___t___", self.tab_space)
        self.replace(xs, "")
    
    
    def quote(self):
        self.replace("'", "\"")
    
    
    def split_list(self):
        return self.html.split("\n")
    
    
    def read(self, file=None):
        if(file != None):
            with open(file, "r", encoding="utf8") as f:
                self.html = f.read()
        else:
            with open(self.read_file, "r", encoding="utf8") as f:
                self.html = f.read()
        self.quote()
        self.split_list()
    
    
    def write(self, file=None):
        if(file != None):
            with open(file, "w", encoding="utf8") as f:
                f.write(self.html)
        else:
            with open(self.write_file, "w", encoding="utf8") as f:
                f.write(self.html)
    
    
    def add_info(self):
        self.html = f"<!-- Brushed up by brushUp.py version:{self.version} -->\n" + self.html
    
    
    def css(self):
        self.replace("""\
    <link rel="stylesheet" href="%scss/main2.css">
    <link rel="stylesheet" href="%scss/main2_half.css" media="screen and (max-width:1360px)">
    <link rel="stylesheet" href="%scss/main2_quarter.css" media="screen and (max-width:850px)">
    <link rel="stylesheet" href="%scss/main2_mobile.css" media="screen and (max-width:550px)">\
"""%(self.read_depth[1], self.read_depth[1], self.read_depth[1], self.read_depth[1]), """\
    <!-- pc版css -->
    <link rel="stylesheet" href="%scss/mainContent.css" media="screen and (min-width:600px)">
    <link rel="stylesheet" href="%scss/sidebar.css" media="screen and (min-width:600px)">
    <link rel="stylesheet" href="%scss/pointerEffect.css" media="screen and (min-width:600px)">
    <link rel="stylesheet" href="%scss/imgContent.css" media="screen and (min-width:600px)">
    <!-- モバイル版css -->
    <link rel="stylesheet" href="%scss/sidebar_mobile.css" media="screen and (max-width:599px)">
    <link rel="stylesheet" href="%scss/mainContent_mobile.css" media="screen and (max-width:599px)">
    <link rel="stylesheet" href="%scss/pointerEffect_mobile.css" media="screen and (max-width:599px)">
    <link rel="stylesheet" href="%scss/imgContent_mobile.css" media="screen and (max-width:599px)">
    <link href='https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css' rel='stylesheet'>\
"""%(self.write_depth[1], self.write_depth[1], self.write_depth[1], self.write_depth[1], self.write_depth[1], self.write_depth[1]))
    
    
    def meta(self, content=None):
        if(content == None):
            self.replace('<meta property="og:type" content="blog">', '<meta property="og:type" content="article">')
        else:
            self.replace('<meta property="og:type" content="blog">', f'<meta property="og:type" content={content}>')


    def js(self):
        self.replace("""<script src="%sjs/main.js"></script>"""%(self.read_depth[1]), """\
    <script src="%sjs/copy.js"></script>
    <script src="%sjs/scroll.js"></script>
    <script src="%sjs/sidebar.js"></script>
    <script src="%sjs/details.js"></script>
    <script src="%sjs/i_btn.js"></script>
    <script src="%sjs/pointerEffect.js"></script>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="%sjs/fade.js"></script>
    <script>
        let topBtn = document.querySelector(".tmTopBtn");
        $(window).on('load scroll', function(){
            if ($(window).scrollTop() > 200) {
                topBtn.classList.add("active");
            } else {
                topBtn.classList.remove("active");
            }
        });
    </script>
    <script src="%scount/count.php"></script>\
"""%(self.write_depth[1], self.write_depth[1], self.write_depth[1],
     self.write_depth[1], self.write_depth[1], self.write_depth[1],
     self.write_depth[1], self.write_depth[1], self.write_depth[1]))
        self.delete("""<script src='//ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>""")
        self.delete("""<script src="%sjs/fade.js"></script>"""%(self.read_depth[1]))
        self.delete("""<script src="%scount/count.php"></script>"""%(self.read_depth[1]))
    
    
    def tab(self):
        self.delete(''' class="tab_now"''')
        self.delete("""<div class="tab">""")
        self.delete("""<p>おさだのホームページ</p>""")
        self.delete("""index.html" id="home">""")
        self.delete("""ホーム\n___t______t______t___</a>""")
        self.delete("""apps.html" id="home">""")
        self.delete("""倉　庫\n___t______t______t___</a>""")
        self.delete("""Remember.html" id="home">""")
        self.delete("""備忘録\n___t______t______t___</a>""")
        self.delete('''blog.html" id="home">''')
        self.delete("""にっき\n___t______t______t___</a>\n___t______t___</div>""")
        
        self.delete("<a href=\n")
        self.delete("<a href=\"../\n")
        self.delete("<a href=\"../../\n")
        self.delete("<a href=\"../../../\n")
        self.delete("<a href=\"blog/\n")
        self.delete("<a href=\"../blog/\n")
        self.delete("<a href=\"../../blog/\n")
        self.delete("<a href=\"Remember/\n")
        self.delete("<a href=\"../Remember/\n")
        self.delete("<a href=\"../../Remember/\n")
        
    
    def delete_only_tab(self):
        result = list()
        for row in self.split_list():
            buf = row.replace(" ", "")
            buf = buf.replace("\t", "")
            buf = buf.replace("\n", "")
            if(len(buf) != 0):
                result.append(row)
        self.html = "\n".join(result)
        
        
    def delete_underground(self):
        result = list()
        for row in self.split_list():
            buf = row.split("___")
            if(len(buf) == 1):
                result.append(row)
        self.html = "\n".join(result)
    
    
    def delete_p_(self):
        result = list()
        for row in self.split_list():
            buf = row.split("<p_>")
            if(len(buf) == 1):
                result.append(row)
        self.html = "\n".join(result)
        result = list()
        for row in self.split_list():
            buf = row.split("</p_>")
            if(len(buf) == 1):
                result.append(row)
        self.html = "\n".join(result)
        result = list()
        for row in self.split_list():
            buf = row.split("<p_ ")
            if(len(buf) == 1):
                result.append(row)
        self.html = "\n".join(result)

    
    def topBtn(self):
        self.replace("""<div id="topScroll" class="tmTopBtn" onclick="tmTopScroll()">▲<br>top</div>""", 
                     """<div class="tmTopBtn" id="topScroll" onclick="tmTopScroll()">
            <i class='bx bx-upvote'></i>
            <br>
            <span class="topScroll_ception">
                top
            </span>
        </div>""")
    
    
    def sidebar(self):
        self.replace("<main>", """<div class="sidebar">
        <div class="logo_content">
            <div class="logo">
                <!-- <i class='bx bxl-python'></i> -->
                <img src="%spic/o_alpha.PNG">
                <div class="name" id="jp_font">
                    おさだのホームページ
                </div>
            </div>
            <i class='bx bx-menu' id="open_btn"></i>
            <i class='bx bx-x' id="close_btn"></i>
        </div>
        <ul class="page_list">
            <!-- search -->
            <li>
                <i class='bx bx-search'></i>
                <input type="text" placeholder="サイト内検索..." id="search-key">
                <i class='bx bx-right-arrow-circle' id="search_btn" onclick="jump()"></i>
            </li>
            <!-- home -->
            <li>
                <a href="%sindex.html">
                    <i class='bx bx-home'></i>
                    <span class="link_name">home</span>
                </a>
                <span class="popup_text">home</span>
            </li>
            <!-- note -->
            <li id="now">
                <a href="%sblog.html">
                    <i class='bx bx-book'></i>
                    <span class="link_name">note</span>
                </a>
                <span class="popup_text">note</span>
            </li>
            <!-- programs -->
            <li>
                <a href="%sapps.html">
                    <i class='bx bx-code-alt'></i>
                    <span class="link_name">programs</span>
                </a>
                <span class="popup_text">programs</span>
            </li>
            <!-- remember -->
            <li>
                <a href="%sRemember/Remember.html">
                    <i class='bx bx-paperclip'></i>
                    <span class="link_name">remember</span>
                </a>
                <span class="popup_text">remember</span>
            </li>
            <li>
                <!-- space -->
            </li>
            <!-- 基本情報技術者試験 -->
            <li>
                <a href="%sjouhou.html">
                    <i class='bx bx-radio-circle'></i>
                    <span class="link_name" id="jp_font">基本情報技術者試験の解答</span>
                </a>
                <span class="popup_text" id="jp_font">基本情報技術者試験の解答</span>
            </li>
            <!-- 文字数カウンター -->
            <li>
                <a href="%stext.html">
                    <i class='bx bx-radio-circle'></i>
                    <span class="link_name" id="jp_font">文字数カウンター</span>
                </a>
                <span class="popup_text" id="jp_font">文字数カウンター</span>
            </li>
            <li></li>
            <!-- secret page -->
            <li id="secret">
                <a href="%smyPage/home.html" target="_blank" rel="noopener noreferrer" id="secret_page">
                    <i class='bx bx-key'></i>
                    <span class="link_name">test page</span>
                </a>
                <span class="popup_text_secret">test page</span>
            </li>
        </ul>
        <div class="profile_content">
            <div class="profile">
                <div class="profile_details">
                    <div class="subscript">Writer</div>
                    <div class="name">
                        Osada Masashi
                        <br>
                        <a href="https://twitter.com/ossa2019_osada" target="_blank" rel="noopener noreferrer">
                            > twitter
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="main_content">"""%(self.write_depth[1], self.write_depth[1], self.blog_depth,
                                   self.write_depth[1], self.write_depth[1], self.write_depth[1],
                                   self.write_depth[1], self.write_depth[1]))
    
    
    def article(self):
        self.replace("""<div class="page">""", "___page___")
        self.replace("""<div class="caption">
                """, "___caption___")
        self.replace("""</div>
            <div class="article">
                <p>""", "___title___")
        self.delete("""</p><br>
                    <section>""")
        caption = "error"
        title = "error"
        for row in self.split_list():
            buf = row.split("___")
            if(len(buf) > 1):
                serector = buf[1]
                if(serector == "caption"):
                    caption = buf[2]
                elif(serector == "title"):
                    title = buf[2]
        self.replace("___page___",
        """<div class="text_content">
            <div class="top_title_text" id="jp_font">おさだのホームページ</div>
            <br>
            <div class="page_title" id="fade_0">
                <div class="title_text">
                    %s
                </div>
                <div class="caption_text" id="jp_font">
                    %s
                </div>
            </div>
            <div class="article">
                <br>"""%(title, caption))

    
    def index(self):
        self.replace("""___t___<div class="a_list">""",
        """<div class="index_content" id="fade_1">
                        <div class="index_link">
                            <span id="jp_font">""")
    
    
    def block(self):
        self.replace("""</div><hr/>""", "</div>")
        self.replace('''<div class="index_title", ''', "___index_id___")
        self.replace('''<div class="index_title" ''', "___index_id___")
        blocks = self.html.split("___index_id___")
        for b in range(len(blocks)):
            index_id = "error"
            for row in self.split_list():
                buf = row.split("___")
                if(len(buf) > 1):
                    serector = buf[1]
                    if(serector == "index_id"):
                        index_id = b
            div_buf = ""
            if(b > 1):
                div_buf = """</span>
                                </div>
                            </div>"""
            blocks[b] = """%s
                        <div class="fade" id="fade_">
                            <div class="title" id="%s">
                            ___index_id_before___"""%(div_buf, index_id) + blocks[b]
            try:
                buf = (blocks[b+1]).split("\n")
                buf = buf[:2] + ["""
                        </div>
                        <div class="text">
                            <span id="jp_font">
                                <br>"""] + buf[3:]
                # buf[1] = buf[1].replace("<br>", "")
                blocks[b+1] = "\n".join(buf)
            except:
                pass
        self.html = "".join(blocks)
    
    
    def det(self):
        self.replace("""<div class="det">""", """<div class="window">
                                <div class="window_btn">
                                    <div class="red"></div>
                                    <div class="yellow"></div>
                                    <div class="green"></div>
                                </div>
                                <div class="window_title">&nbsp;</div>
                                <div class="window_content" id="explain">
                                    <div class="window_content_buf" id="explain"></div>
                                    <div class="window_text">
                                        <span id="jp_font">""")
    
    
    def code(self):
        self.replace("""<div class="code">""", """<div class="code_window_details" id="window_">
                                <div class="window_btn">
                                    <div class="red"></div>
                                    <div class="yellow"></div>
                                    <div class="green"></div>
                                    <div class="copy_btn" id="copy_btn" onclick="onClickCopy('copy_text_', 'popup_')">copy</div>
                                    <div class="copied" id="popup_">copied!</div>
                                </div>
                                <div class="window_title">make_rsa.py</div>
                                <div class="window_content">
                                    <div class="details_btn" id="details_btn" onclick="details_activate('window_')">
                                        <i class='bx bxs-chevron-down' id="openClose_btn"></i>
                                        <div class="details_btn_text" id="jp_font">展開</div>
                                        <div class="details_btn_text_opened" id="jp_font">折り畳む</div>
                                    </div>
                                    <div class="window_content_buf"></div>
                                    <div class="window_text">
                                        <span id="copy_text_">""")
    
    
    def window_close(self):
        is_window = False
        is_text = False
        span_count = 0
        result = list()
        for row in self.split_list():
            buf = row.replace(" ", "")
            buf = buf.replace("\t", "")
            if(is_window) or (is_text):
                if("<span" in buf):
                    span_count += 1
                if("</span" in buf):
                    span_count -= 1
                if(buf in ["</div>", "</div><br>"]):
                    is_text = False
                    span_buf = """
                            </span>""" * span_count
                    result.append(span_buf)
                    span_count = 0
                    result.append("""
                        </div>
                    </div>""")
                else:
                    is_text = True
            is_window = buf == '<divclass="window_text">'
            result.append(row)
        self.html = "\n".join(result)
        
    
    def delete_details(self):
        self.replace("<details>", "<!-- <details> -->")
        self.replace("</details>", "<!-- </details> -->")
        self.replace("<summary>", "<!-- <summary> -->")
        self.replace("</summary>", "<!-- </summary> -->")
    
    
    def revive_doctype(self):
        buf = ["<!DOCTYPE html>"] + self.split_list()[2:]
        self.html = "\n".join(buf)
    
    
    def output(self):
        print(f"\n{self.read_file} -> {self.write_file}\n")

            
    def do_all(self, read, write):
        self.set_file(read, write)
        
        self.css()
        self.js
        self.meta()
        self.tab()
        self.topBtn()
        self.sidebar()
        self.article()
        self.index()
        self.block()
        self.det()
        self.code()
        self.window_close()
        
        self.delete_details()
        self.delete_only_tab()
        self.delete_underground()
        self.delete_p_()
        
        self.revive_doctype()
        
        self.add_info()
        
        self.write()
        
        self.output()


name = "chromeEx1"

old_html = f"blog/chromeEx/{name}.html"
new_html = f"blog/chromeEx/{name}_new.html"

html = myHtml()
html.do_all(old_html, new_html)
