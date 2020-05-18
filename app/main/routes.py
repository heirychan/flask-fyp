from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from sqlalchemy import func
from app import current_app, db
from app.main.forms import EditProfileForm, PostForm
from app.models import User, Post, News, Tech, Anime, Network, Evaluation, \
    Ittime, Reward, Video, Ads, Special, Editor, Extend
from app.main import bp


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/ez ', methods=['GET', 'POST'])
def ez():
    all = News.query.order_by(News.time.desc()).all()
    tech = Tech.query.order_by(func.random()).limit(4)
    hot = Video.query.order_by(func.random()).limit(4)
    network = Network.query.order_by(func.random()).limit(4)
    anime = Anime.query.order_by(func.random()).limit(4)
    evaluation = Evaluation.query.order_by(func.random()).limit(4)
    itttime = Ittime.query.order_by(func.random()).limit(4)
    ads = Ads.query.filter_by(big=False).order_by(func.random()).limit(1)
    adsb = Ads.query.filter_by(big=True).order_by(func.random()).limit(1)
    edit = Editor.query.order_by(func.random()).all()
    return render_template('ez.html', title=_('E-Zone'), all=all, tech=tech, hot=hot, network=network,
                           anime=anime, evaluation=evaluation, itttime=itttime, ads=ads, adsb=adsb,
                           edit=edit)


@bp.route('/<st_category>/<nd_category>/<table>', methods=['GET', 'POST'])
def topic(st_category, nd_category, table):
    all = News.query.order_by(News.time.desc()).all()
    ads = Ads.query.filter_by(big=False).order_by(func.random()).limit(1)
    adsb = Ads.query.filter_by(big=True).order_by(func.random()).limit(1)
    edit = Editor.query.order_by(func.random()).all()
    if table == 'TF':
        if nd_category == 'None':
            news = Tech.query.all()
        else:
            news = Tech.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    elif table == 'NET':
        if nd_category == 'None':
            news = Network.query.all()
        else:
            news = Network.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    elif table == 'ANI':
        if nd_category == 'None':
            news = Anime.query.all()
        else:
            news = Anime.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    elif table == 'EVA':
        if nd_category == 'None':
            news = Evaluation.query.all()
        else:
            news = Evaluation.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    elif table == 'ITT':
        if nd_category == 'None':
            news = Ittime.query.all()
        else:
            news = Ittime.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    elif table == 'RW':
        news = Reward.query.all()
    elif table == 'SP':
        news = Special.query.all()
    else:
        news = Video.query.all()
    return render_template('topic.html', title=_('E-Zone'), all=all, news=news, st_cat=st_category,
                           nd_cat=nd_category, table=table, ads=ads, adsb=adsb, edit=edit)


@bp.route('/<content>/<picture>', methods=['GET', 'POST'])
def tfb(content, picture):
    table = ""
    all = News.query.order_by(News.time.desc()).all()
    ads = Ads.query.filter_by(big=False).order_by(func.random()).limit(1)
    adsb = Ads.query.filter_by(big=True).order_by(func.random()).limit(1)
    body = Extend.query.filter_by(picture_name=picture).all()
    tech = Tech.query.filter_by(picture_name=picture).all()
    hot = Video.query.filter_by(picture_name=picture).all()
    network = Network.query.filter_by(picture_name=picture).all()
    anime = Anime.query.filter_by(picture_name=picture).all()
    evaluation = Evaluation.query.filter_by(picture_name=picture).all()
    itttime = Ittime.query.filter_by(picture_name=picture).all()
    if table == "":
        for result in tech:
            table = result.st_cat
        news = Tech.query.filter(~Tech.picture_name.in_([picture])).order_by(func.random()).limit(2)
    if table == "":
        for result in hot:
            table = result.st_cat
        hots = Video.query.filter_by(picture_name=picture).all()
        news = Video.query.filter(~Video.picture_name.in_([picture])).order_by(func.random()).limit(2)
    if table == "":
        for result in network:
            table = result.st_cat
        news = Network.query.filter(~Network.picture_name.in_([picture])).order_by(func.random()).limit(2)
    if table == "":
        for result in anime:
            table = result.st_cat
        news = Anime.query.filter(~Anime.picture_name.in_([picture])).order_by(func.random()).limit(2)
    if table == "":
        for result in evaluation:
            table = result.st_cat
        news = Evaluation.query.filter(~Evaluation.picture_name.in_([picture])).order_by(func.random()).limit(2)
    if table == "":
        for result in itttime:
            table = result.st_cat
        news = Ittime.query.filter(~Ittime.picture_name.in_([picture])).order_by(func.random()).limit(2)
    return render_template('TFocus/TFB.html', title=_('E-Zone'), all=all, ads=ads, adsb=adsb, body=body,
                           content=content, picture=picture, news=news, table=table, hots=hots)


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/flous ', methods=['GET', 'POST'])
@login_required
def flous():
    return render_template('flous.html', title=_('E-Zone'))


@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title=_('Home'), form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/greencar', methods=['GET', 'POST'])
@login_required
def greencar():
    return render_template('video/greencar.html', title=_('car'))


@bp.route('/ccmask', methods=['GET', 'POST'])
@login_required
def ccmask():
    return render_template('video/ccmask.html', title=_('ccmask'))


@bp.route('/fever', methods=['GET', 'POST'])
@login_required
def fever():
    return render_template('video/fever.html', title=_('fever'))


@bp.route('/sptmask', methods=['GET', 'POST'])
@login_required
def sptmask():
    return render_template('video/sptmask.html', title=_('sptmask'))


@bp.route('/intel', methods=['GET', 'POST'])
@login_required
def intel():
    return render_template('itt/new/intel.html', title=_('Intel'))


@bp.route('/covid', methods=['GET', 'POST'])
@login_required
def covid():
    return render_template('itt/new/covid.html', title=_('COVID'))


@bp.route('/wifi', methods=['GET', 'POST'])
@login_required
def wifi():
    return render_template('itt/onlyme/wifi.html', title=_('WIFI'))


@bp.route('/vm', methods=['GET', 'POST'])
@login_required
def vm():
    return render_template('itt/onlyme/vm.html', title=_('vmware'))


@bp.route('/moon', methods=['GET', 'POST'])
@login_required
def sailor():
    return render_template('animax/anime/sailormoon.html', title=_('美少女戰士'))


@bp.route('/Sumikko Gurashi', methods=['GET', 'POST'])
@login_required
def sg():
    return render_template('reward/sg.html', title=_('角落小夥伴'))


@bp.route('/ucc', methods=['GET', 'POST'])
@login_required
def ucc():
    return render_template('animax/anime/ucc.html', title=_('新世紀福音戰士'))


@bp.route('/tokyo', methods=['GET', 'POST'])
@login_required
def tokyo():
    return render_template('animax/game/tokyo.html', title=_('TGS2020'))


@bp.route('/ps5', methods=['GET', 'POST'])
@login_required
def ps5():
    return render_template('animax/game/ps5.html', title=_('PS5'))


@bp.route('/emoji', methods=['GET', 'POST'])
@login_required
def emoji():
    return render_template('evaluation/apply/emoji.html', title=_('Emoji'))


@bp.route('/pcandroid', methods=['GET', 'POST'])
@login_required
def pcandroid():
    return render_template('evaluation/apply/pcandroid.html', title=_('模擬器'))


@bp.route('/blacksha', methods=['GET', 'POST'])
@login_required
def blacksha():
    return render_template('evaluation/newtest/blacksha.html', title=_('黑鯊 3 電競手機'))


@bp.route('/sama31', methods=['GET', 'POST'])
@login_required
def sama31():
    return render_template('evaluation/newtest/sama31.html', title=_('Samsung Galaxy A31'))


@bp.route('/computer', methods=['GET', 'POST'])
@login_required
def computer():
    return render_template('special/computer.html', title=_('香港電腦通訊節'))


@bp.route('/featured', methods=['GET', 'POST'])
@login_required
def featured():
    return render_template('editor/featured.html', title=_('未來戰士'))


@bp.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title=_('Explore'),
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=_('Edit Profile'),
                           form=form)


@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash(_('You cannot follow yourself!'))
        return redirect(url_for('main.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(_('You are following %(username)s!', username=username))
    return redirect(url_for('main.user', username=username))


@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash(_('You cannot unfollow yourself!'))
        return redirect(url_for('main.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash(_('You are not following %(username)s.', username=username))
    return redirect(url_for('main.user', username=username))
