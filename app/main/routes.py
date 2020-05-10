from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import current_app, db
from app.main.forms import EditProfileForm, PostForm
from app.models import User, Post, News, Tech, Anime, Network, Evaluation, Ittime
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
    all = News.query.all()
    return render_template('ez.html', title=_('E-Zone'), all=all)


@bp.route('/<st_category>/<nd_category>/<table>', methods=['GET', 'POST'])
def tf(st_category, nd_category, table):
    if table == 'TF':
        if nd_category == 'None':
            all = Tech.query.all()
        else:
            all = Tech.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    elif table == 'NET':
        if nd_category == 'None':
            all = Network.query.all()
        else:
            all = Network.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    elif table == 'ANI':
        if nd_category == 'None':
            all = Anime.query.all()
        else:
            all = Anime.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    elif table == 'EVA':
        if nd_category == 'None':
            all = Evaluation.query.all()
        else:
            all = Evaluation.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    else:
        if nd_category == 'None':
            all = Ittime.query.all()
        else:
            all = Ittime.query.filter_by(st_cat=st_category, nd_cat=nd_category)
    return render_template('TF.html', title=_('ezone'), all=all,
                           st_cat=st_category, nd_cat=nd_category, table=table)


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


@bp.route('/seveneleven', methods=['GET', 'POST'])
@login_required
def seveneleven():
    return render_template('Network/life/7-11.html', title=_('7-11'))


@bp.route('/intel10', methods=['GET', 'POST'])
@login_required
def intel10():
    return render_template('TFocus/PC/intel10.html', title=_('intel10'))


@bp.route('/winup', methods=['GET', 'POST'])
@login_required
def winup():
    return render_template('TFocus/PC/winup.html', title=_('Windowupdate'))


@bp.route('/sm', methods=['GET', 'POST'])
@login_required
def sm():
    return render_template('TFocus/phone/sm.html', title=_('Samsung'))


@bp.route('/ipxs', methods=['GET', 'POST'])
@login_required
def ipxs():
    return render_template('TFocus/phone/ipxs.html', title=_('IPhoneXS'))


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


@bp.route('/omask', methods=['GET', 'POST'])
@login_required
def omask():
    return render_template('Network/hot/omask.html', title=_('開窿口罩'))


@bp.route('/av', methods=['GET', 'POST'])
@login_required
def av():
    return render_template('Network/hot/av.html', title=_('睇 AV 出「意外」！'))


@bp.route('/dyson', methods=['GET', 'POST'])
@login_required
def dyson():
    return render_template('Network/life/dyson.html', title=_('Dyson 旗艦體'))


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
