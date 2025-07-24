# HTMLコードレビューの観点 - 基礎から実務レベルまで

## はじめに

HTML研修やコードレビューを担当していると、「何をどこまでチェックすればいいの？」という質問をよく受けます。初学者向けの基礎的なチェックポイントから、実務レベルで求められる高度な観点まで、段階的にまとめてみました。

実際の課題ファイルを例にして、「基礎版」と「プロ版」の違いを具体的に解説します。

## 📝 アウトラインで見るHTML構造

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/7eeab784-176c-4456-85cb-10edcda2e7f7.png)

### 🎯 模範解答版

基本的なHTMLタグの使い方を習得する段階での目標レベルです。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>犬の一生</title>
</head>
<body>
    <h1>犬の一生</h1>
    <p>犬は古くから人類と共存し、単なるペットではなく家族の一員として、かけがえのない存在です。その一生は、喜びと成長、そして人間との深い絆の中で築かれます。<br>
        このレポートでは、犬のライフステージとその特徴、人間との関わりについて掘り下げます。犬の一生を理解することは、彼らが健康で幸せに過ごすための第一歩となるでしょう。</p>
    
    <figure>
        <img src="images/dog.jpg" alt="">
        <figcaption>犬と人間は古くから共存してきた</figcaption>
    </figure>
    
    <hr>
    <h2>成長の段階</h2>
    <p>犬の成長はいくつかの段階を経て進み、それぞれ必要なケアやしつけが異なります。ここでは、犬の一生を特徴的な4つのフェーズに分けて解説します。各時期の特性を理解し、愛犬が健やかに成長できるようサポートしましょう。</p>
    
    <ol>
        <li>子犬期（0〜6ヶ月）：誕生、離乳、社会化の重要性、しつけの基礎</li>
        <li>青年期（6ヶ月〜2歳）：体の成長、性成熟、精神的な発達、問題行動への対処</li>
        <li>成犬期（2歳〜7歳）：安定した時期、健康管理、適度な運動と遊び</li>
        <li>老犬期（7歳〜）：体の変化、介護の必要性、終末期のケア</li>
    </ol>
    
    <h3>子犬期（0〜6ヶ月）</h3>
    <p>心身の基礎が形成される重要な時期。社会性や基本的なしつけを身につけ、信頼関係を築くことが大切です。ワクチン接種や健康チェックも欠かせません。</p>
    
    <!-- 他の成長段階も同様 -->
    
    <hr>
    <h2>健康と病気</h2>
    <p>犬の健康維持には、日頃の観察と適切なケアが不可欠です。食欲や元気さなど、常に状態を確認しましょう。定期的な予防接種や寄生虫予防は、病気から犬を守るために重要です。年齢や犬種に合わせた食事、運動、そして定期健診も欠かせません。異変を感じたら、すぐに獣医師に相談しましょう。</p>
    
    <p>犬の病気について詳しくは<a href="https://www.fpc-pet.co.jp/dog/disease" target="_blank">こちら</a>をご覧ください。</p>
    
    <!-- 残りのセクションも同様 -->
</body>
</html>
```

### 🚀 実務ではこう書く

実際のWebサイト制作で求められるクオリティです。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="犬のライフステージと特徴、人間との関わりについて詳しく解説したレポート。子犬期から老犬期まで、各成長段階での適切なケア方法をご紹介します。">
    <meta name="keywords" content="犬, ペット, ライフステージ, 成長段階, 健康管理, しつけ">
    <meta name="author" content="ペット情報センター">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="犬の一生 - ライフステージ別ケアガイド">
    <meta property="og:description" content="犬のライフステージと特徴、人間との関わりについて詳しく解説したレポート">
    <meta property="og:image" content="images/dog.jpg">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="犬の一生 - ライフステージ別ケアガイド">
    <meta name="twitter:description" content="犬のライフステージと特徴、人間との関わりについて詳しく解説したレポート">
    
    <title>犬の一生 - ライフステージ別ケアガイド | ペット情報センター</title>
    
    <!-- 構造化データ -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "犬の一生 - ライフステージ別ケアガイド",
        "description": "犬のライフステージと特徴、人間との関わりについて詳しく解説したレポート",
        "image": "images/dog.jpg",
        "author": {
            "@type": "Organization",
            "name": "ペット情報センター"
        },
        "publisher": {
            "@type": "Organization",
            "name": "ペット情報センター"
        },
        "datePublished": "2024-07-24"
    }
    </script>
</head>

<body>
    <header role="banner">
        <nav aria-label="メインナビゲーション">
            <!-- ナビゲーションは実装時に追加 -->
        </nav>
    </header>

    <main role="main">
        <article>
            <header>
                <h1>犬の一生</h1>
                <p class="lead">犬は古くから人類と共存し、単なるペットではなく家族の一員として、かけがえのない存在です。その一生は、喜びと成長、そして人間との深い絆の中で築かれます。<br>
                    このレポートでは、犬のライフステージとその特徴、人間との関わりについて掘り下げます。犬の一生を理解することは、彼らが健康で幸せに過ごすための第一歩となるでしょう。</p>
            </header>

            <figure role="img" aria-labelledby="hero-caption">
                <img src="images/dog.jpg" alt="人間の家族と一緒に過ごす犬の写真。リビングルームで子供たちと遊んでいる様子" loading="lazy" width="800" height="400">
                <figcaption id="hero-caption">犬と人間は古くから共存してきた</figcaption>
            </figure>

            <section aria-labelledby="growth-stages">
                <h2 id="growth-stages">成長の段階</h2>
                <p>犬の成長はいくつかの段階を経て進み、それぞれ必要なケアやしつけが異なります。ここでは、犬の一生を特徴的な4つのフェーズに分けて解説します。各時期の特性を理解し、愛犬が健やかに成長できるようサポートしましょう。</p>
                
                <ol role="list" aria-label="犬の成長段階">
                    <li>子犬期（0〜6ヶ月）：誕生、離乳、社会化の重要性、しつけの基礎</li>
                    <li>青年期（6ヶ月〜2歳）：体の成長、性成熟、精神的な発達、問題行動への対処</li>
                    <li>成犬期（2歳〜7歳）：安定した時期、健康管理、適度な運動と遊び</li>
                    <li>老犬期（7歳〜）：体の変化、介護の必要性、終末期のケア</li>
                </ol>

                <article aria-labelledby="puppy-stage">
                    <h3 id="puppy-stage">子犬期（0〜6ヶ月）</h3>
                    <p>心身の基礎が形成される重要な時期。社会性や基本的なしつけを身につけ、信頼関係を築くことが大切です。ワクチン接種や健康チェックも欠かせません。</p>
                </article>

                <!-- 他の成長段階も同様の構造 -->
            </section>

            <section aria-labelledby="health-disease">
                <h2 id="health-disease">健康と病気</h2>
                <p>犬の健康維持には、日頃の観察と適切なケアが不可欠です。食欲や元気さなど、常に状態を確認しましょう。定期的な予防接種や寄生虫予防は、病気から犬を守るために重要です。年齢や犬種に合わせた食事、運動、そして定期健診も欠かせません。異変を感じたら、すぐに獣医師に相談しましょう。</p>
                
                <p>犬の病気について詳しくは<a href="https://www.fpc-pet.co.jp/dog/disease" target="_blank" rel="noopener noreferrer" aria-describedby="external-link-desc">アニコム損保の犬の病気ガイド<span class="sr-only">（外部サイト）</span></a>をご覧ください。</p>
                <div id="external-link-desc" class="sr-only">このリンクは外部サイトに移動します</div>
            </section>

            <!-- 他のセクションも同様の構造 -->
        </article>
    </main>

    <footer role="contentinfo">
        <p><small>&copy; 2024 ペット情報センター. All rights reserved.</small></p>
    </footer>
</body>
</html>
```

## 📋 レベル別チェックポイント

### 🎯 基礎レベル（今日のゴール）

#### 1. 基本構造の確認
- [ ] DOCTYPE宣言があるか
- [ ] html要素にlang属性が設定されているか
- [ ] head内に必要最低限のmeta要素があるか（charset, viewport）
- [ ] title要素が空でないか

#### 2. 見出し構造の確認
- [ ] h1タグが1つだけ使われているか
- [ ] 見出しの階層が論理的か（h1→h2→h3の順序）
- [ ] 見出しレベルを飛ばしていないか

#### 3. コンテンツの構造化
- [ ] 段落はp要素で囲まれているか
- [ ] リストが適切に使われているか（ol vs ul）
- [ ] 画像にalt属性があるか（空でも可）
- [ ] 外部リンクにtarget="_blank"が設定されているか

#### 4. HTML記法の正確性
- [ ] タグが正しく閉じられているか
- [ ] 入れ子構造が正しいか
- [ ] 必須属性が抜けていないか

**このレベルでの指導ポイント**
```
❌ 避けるべきフィードバック
「セマンティックHTMLを意識して」（まだ早い）
「アクセシビリティを考慮して」（概念が理解できない）

✅ 効果的なフィードバック
「見出しは大きい順に使いましょう」
「この部分はリストにできそうですね」
「alt属性を追加してみましょう」
```

### 🚀 実務レベル

#### 1. SEO・メタデータの最適化
- [ ] meta description が適切に設定されているか（120-160文字）
- [ ] title要素がSEOを意識した内容になっているか
- [ ] Open Graph / Twitter Card が設定されているか
- [ ] 構造化データ（JSON-LD）が実装されているか

#### 2. セマンティックHTML
- [ ] HTML5のセマンティック要素が適切に使われているか
  - `<main>`, `<article>`, `<section>`, `<header>`, `<footer>`, `<nav>`
- [ ] コンテンツの意味に適した要素が選ばれているか
- [ ] 文書のアウトライン構造が論理的か

#### 3. アクセシビリティ（WCAG準拠）
- [ ] WAI-ARIA属性が適切に使われているか
  - `role`, `aria-labelledby`, `aria-describedby`, `aria-label`
- [ ] キーボードナビゲーションが考慮されているか
- [ ] スクリーンリーダー向けの配慮があるか
- [ ] 色だけに依存しない情報提供ができているか

#### 4. パフォーマンス・UX
- [ ] 画像の最適化（loading="lazy", width/height属性）
- [ ] 外部リンクのセキュリティ（rel="noopener noreferrer"）
- [ ] レスポンシブデザインへの配慮
- [ ] Core Web Vitalsを意識した実装

#### 5. 保守性・チーム開発
- [ ] 一貫した命名規則が使われているか
- [ ] コメントが適切に書かれているか
- [ ] 再利用可能な構造になっているか
- [ ] HTMLバリデーションが通るか

## 🔍 具体的なレビューの進め方

### 段階的アプローチ

1. **基礎チェック** → HTML文法、基本構造
2. **意味チェック** → セマンティック、コンテンツ構造
3. **体験チェック** → アクセシビリティ、UX
4. **技術チェック** → SEO、パフォーマンス

### レビューコメントの例

#### ❌ 改善の余地があるコメント
```
「アクセシビリティがダメです」
「セマンティックHTMLを使ってください」
「SEOを考慮してください」
```

#### ✅ 建設的なコメント
```
「h2の後にh4が来ています。h3を使いましょう」
「この画像のalt属性で、どんな写真かを具体的に説明してみてください」
「このリンクは外部サイトなので、target="_blank"とrel="noopener"を追加することをお勧めします」
```

## 💡 レベル判定の目安

| レベル | チェック内容 | 期待する成果物 |
|--------|------------|--------------|
| **基礎** | HTML文法、基本タグ | 構造化された読みやすいHTML |
| **中級** | セマンティック要素、SEO基礎 | 検索エンジンに理解されやすいHTML |
| **上級** | アクセシビリティ、パフォーマンス | 誰でも使いやすい高品質なHTML |
| **プロ** | チーム開発、保守性、最新仕様 | 本格的なWebサイトレベル |

## 🎓 指導する際のコツ

### 段階的な成長を促す

1. **基礎固め期**：完璧を求めすぎない、基本の定着を重視
2. **応用発展期**：なぜそのタグを選ぶかの理由を考えさせる
3. **実践活用期**：実際のWebサイトと比較させる
4. **プロ志向期**：チーム開発や保守性まで考慮させる

### よくある間違いとその対処

```html
<!-- ❌ よくある間違い -->
<h1>メインタイトル</h1>
<h3>サブタイトル</h3>  <!-- h2を飛ばしている -->

<!-- ✅ 正しい構造 -->
<h1>メインタイトル</h1>
<h2>サブタイトル</h2>
```

```html
<!-- ❌ 装飾目的での使用 -->
<h1>小さく見せたいけど重要なタイトル</h1>

<!-- ✅ 意味に基づいた使用 -->
<h2>適切なレベルのタイトル</h2>
```

## まとめ

HTMLのコードレビューは、単なる文法チェックではありません。学習者のレベルに応じて適切な観点でレビューし、段階的に成長をサポートすることが重要です。

基礎段階では「正しく動くHTML」を、実務レベルでは「ユーザーにとって価値のあるHTML」を目指しましょう。そして何より、**なぜその書き方をするのか**という理由を理解してもらうことが、長期的な成長につながります。

---

### 参考資料

- [HTML Living Standard](https://html.spec.whatwg.org/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Web Docs](https://developer.mozilla.org/ja/docs/Web/HTML)
- [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)
