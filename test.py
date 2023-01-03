html = """<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" type="image/png" href="/static/img/favicon-32x32.png" sizes="32x32"><link rel="icon" type="image/png" href="/static/img/favicon-16x16.png" sizes="16x16"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css?family=Material+Icons&display=block" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Overpass+Mono:wght@400;700&family=Overpass:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet"><meta charset="utf-8"><title id="title">OSV</title><script async src="https://www.googletagmanager.com/gtag/js?id=G-ZXG9G6HTBR"></script><script>window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-ZXG9G6HTBR', { 'anonymize_ip': true });</script><script defer="defer" src="/static/vendors.af77356522aaacbd358e.js"></script><script defer="defer" src="/static/main.94c62785e419319c616f.js"></script><link href="/static/main.47829387a5541cab6c31.css" rel="stylesheet"></head><body><div class="wrapper "><header class="top-bar"><div class="logo"><a href="/"><img src="/static/img/logo.png" srcset="/static/img/logo.png, /static/img/logo@2x.png 2x"></a></div><input type="checkbox" id="hamburger-checkbox"> <label class="hamburger" for="hamburger-checkbox"><span></span> <span></span> <span></span></label><ul class="tabs"><li class="active page-link"><a href="/list">Vulnerability Database</a></li><li class=" page-link"><a href="/blog/">Blog</a></li><li class=" page-link"><a href="/about">About</a></li><li class="push"><a class="logo-img" href="https://github.com/google/osv.dev" target="_blank"><img class="logo-link" src="/static/img/github-mark-white.svg"></a></li></ul></header>
<div class="vulnerability-page">
<div class="mdc-layout-grid">
  <div class="mdc-layout-grid__inner">
    <div class="mdc-layout-grid__cell--span-12">
      <h1 class="title">OSV-2022-714</h1>
    </div>
    <div class="mdc-layout-grid__cell--span-12">
      <dl class="vulnerability-details">
        <dt>Source</dt>
        <dd><a href="https://github.com/google/oss-fuzz-vulns/blob/main/vulns/libredwg/OSV-2022-714.yaml">https://github.com/google/oss-fuzz-vulns/blob/main/vulns/libredwg/OSV-2022-714.yaml</a></dd>

        <dt>Published</dt>
        <dd>2022-08-15T00:00:47.794062Z</dd>
        <dt>Modified</dt>
        <dd>2023-01-03T00:31:18.613990Z</dd>
        <dt>Details</dt>
        <dd class="details">
          <p>OSS-Fuzz report: https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=50194</p>

<pre><code>Crash type: Heap-buffer-overflow WRITE 16
Crash state:
dynapi_set_helper
dwg_dynapi_header_set_value
json_HEADER
</code></pre>

        </dd>
        <dt>References</dt>
        <dd>
          <ul class="links">

              <li><a href="https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=50194">https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=50194</a></li>

          </ul>
        </dd>
      </dl>
    </div>
  </div>
</div>
<div class="vulnerability-packages-container">
  <h2 class="title">Affected packages</h2>
  <spicy-sections
      class="vulnerability-packages">

      <h2 class="package-header">
        <span class="vuln-ecosystem spicy-sections-workaround">OSS-Fuzz</span>
        <span class="vuln-title-divider spicy-sections-workaround">/</span>
        <span class="vuln-name spicy-sections-workaround">libredwg</span>
      </h2>
      <div class="mdc-layout-grid">
        <p class="subtitle">libredwg</p>
        <div class="vulnerability-package-subsection mdc-layout-grid__inner">
          <h3 class="mdc-layout-grid__cell--span-3">
            Affected ranges
            <a href="https://ossf.github.io/osv-schema/#examples"></a>
          </h3>
          <div class="mdc-layout-grid__cell--span-9">

              <dl>
                <dt>Type</dt>
                <dd>GIT</dd>
                <dt>Events</dt>
                <dd>
                  <div class="mdc-layout-grid__inner events">

                      <div class="mdc-layout-grid__cell--span-3">
                        Introduced
                      </div>
                      <div class="mdc-layout-grid__cell--span-9 version-value">


                          <a href="https://github.com/LibreDWG/libredwg/commit/8984c223f14dc81180ca5da66f92e5932992bb5c"}>


                        8984c223f14dc81180ca5da66f92e5932992bb5c


                          </a>

                      </div>

                  </div>
                </dd>
              </dl>

          </div>
        </div>
        <div class="vulnerability-package-subsection mdc-layout-grid__inner">
          <h3 class="mdc-layout-grid__cell--span-3">
            Affected versions
            <a href="https://ossf.github.io/osv-schema/#affectedversions-field"></a>
          </h3>
          <div class="mdc-layout-grid__cell--span-9 version-value">

              <spicy-sections class="versions-section">
                <h2 class="version-header">0.*</h2>
                <div class="versions ">

                    <div class="version">0.12.4.4635</div>

                    <div class="version">0.12.4.4637</div>

                    <div class="version">0.12.4.4641</div>

                    <div class="version">0.12.4.4643</div>

                    <div class="version">0.12.4.4647</div>

                    <div class="version">0.12.4.4652</div>

                    <div class="version">0.12.4.4654</div>

                    <div class="version">0.12.4.4658</div>

                    <div class="version">0.12.4.4660</div>

                    <div class="version">0.12.4.4668</div>

                    <div class="version">0.12.5.4669</div>

                    <div class="version">0.12.5.4678</div>

                    <div class="version">0.12.5.4685</div>

                    <div class="version">0.12.5.4690</div>

                    <div class="version">0.12.5.4693</div>

                    <div class="version">0.12.5.4695</div>

                    <div class="version">0.12.5.4697</div>

                    <div class="version">0.12.5.4700</div>

                    <div class="version">0.12.5.4709</div>

                    <div class="version">0.12.5.4712</div>

                    <div class="version">0.12.5.4715</div>

                    <div class="version">0.12.5.4722</div>

                    <div class="version">0.12.5.4724</div>

                    <div class="version">0.12.5.4726</div>

                    <div class="version">0.12.5.4731</div>

                    <div class="version">0.12.5.4735</div>

                    <div class="version">0.12.5.4739</div>

                    <div class="version">0.12.5.4741</div>

                    <div class="version">0.12.5.4743</div>

                    <div class="version">0.12.5.4748</div>

                    <div class="version">0.12.5.4750</div>

                    <div class="version">0.12.5.4756</div>

                    <div class="version">0.12.5.4760</div>

                    <div class="version">0.12.5.4763</div>

                    <div class="version">0.12.5.4765</div>

                    <div class="version">0.12.5.4772</div>

                    <div class="version">0.12.5.4776</div>

                    <div class="version">0.12.5.4780</div>

                    <div class="version">0.12.5.4784</div>

                    <div class="version">0.12.5.4787</div>

                </div>
              </spicy-sections>

          </div>
        </div>

          <div class="vulnerability-package-subsection mdc-layout-grid__inner">
            <h3 class="mdc-layout-grid__cell--span-3">
              Ecosystem specific
              <a href="https://ossf.github.io/osv-schema/#affectedecosystem_specific-field"></a>
            </h3>
            <div class="mdc-layout-grid__cell--span-9">
              <pre class="specific">{
    &#34;severity&#34;: &#34;HIGH&#34;
}</pre>
            </div>
          </div>


      </div>

  </spicy-sections>
</div>
</div>
<turbo-stream action="update" target="title">
  <template>
    OSV-2022-714 - OSV
  </template>
</turbo-stream>
</div></body></html>"""

import random
import requests
import time
import re
from bs4 import BeautifulSoup
from ua_info import ua_list


class OSVspider(object):
    def get_detail(self):
        soup = BeautifulSoup(html, 'html.parser')
        item = {}
        title = soup.find('h1', class_='title').text
        item['title'] = title
        target = soup.find('dl', class_='vulnerability-details')
        dt_pattern = 'dt:nth-of-type({})'
        dd_pattern = 'dd:nth-of-type({})'
        i = 1
        while 1:
            check = target.select(dt_pattern.format(str(i)))
            if not check:
                break
            raw_name = str(check[0])
            dt_reg = '<dt>(.*?)</dt>'
            name = re.compile(dt_reg, re.S).findall(raw_name)[0]
            if name == 'Details':
                value_list = target.find_all(['p', 'code'])
                value = []
                for v in value_list:
                    value.append(v.text.strip())

            elif name == 'References':
                raw_value = target.select(dd_pattern.format(str(i)))[0]
                value = raw_value.find('a', href=True).text
            else:
                raw_value = str(target.select(dd_pattern.format(str(i)))[0])
                dd_reg = '<dd>(.*?)</dd>'
                value = re.compile(dd_reg, re.S).findall(raw_value)[0]
            if i == 1:
                value = re.compile('<a href.*?>(.*?)</a>', re.S).findall(value)[0]
            item[name] = value
            i += 1
        pass


if __name__ == '__main__':
    start = time.time()
    agent = OSVspider()
    agent.get_detail()
    end = time.time()